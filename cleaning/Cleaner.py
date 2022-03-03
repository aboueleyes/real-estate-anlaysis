from typing import Tuple
import pandas as pd
import numpy as np
import logging
from tqdm import tqdm
import re


class Cleaner:
    '''
    A class made for cleaning data related to olx
    '''

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
        self.logger.info('Cleaner initialized')

    def __get_governorates_cities(self, location: pd.Series) -> dict:
        """returns a dictionary of governorates and cities
        Args:
            df (pd.DataFrame): a location df

        Returns:
            dict: governrate and cities mapping
        """
        cities = {}
        single_cities = []
        for loc in tqdm(location.unique()):
            if loc != loc:
                continue
            x = re.split(r',|،', loc)
            if len(x) == 2:
                cities[x[0]] = x[1]
            else:
                single_cities.append(loc)
        for city in single_cities:
            if city not in cities:
                self.logger.error(f'{city} not in cities')
                cities[city] = 'error city'
        return cities

    @staticmethod
    def __get_city(city: str) -> str:
        """
        Gets the city from a location
        Args:
            city (str): a location

        Returns:
            str: the city
        """
        if city != city:
            return city
        return re.split(r',|،', city)[0].strip()

    @staticmethod
    def __get_governorate(city: str, cities: dict) -> str:
        """
        Gets the governorate from a location
        Args:
            city (str): a location

        Returns:
            str: the governorate
        """
        if city != city:
            return city
        return cities[re.split(r',|،', city)[0]].strip()

    def __get_region(self, city: str) -> str:
        regions = {'Capital': ['Cairo', 'Giza'],
                   'Alexandria': ['Alexandria'],
                   'Canal': ['Port Said', 'Ismailia', 'Suez'],
                   'Upper Egypt': ['Sohag', 'Aswan', 'Minya', 'Luxor', 'Asyut', 'Qena', 'Beni Suef', 'Fayoum'],
                   'Lower Egypt': ['Qalyubia', 'Dakahlia', 'Gharbia', 'Beheira', 'Monufia', 'Kafr al-Sheikh', 'Damietta', 'Sharqia'],
                   'Border': ['Red Sea', 'South Sinai', 'New Valley', 'Matruh', 'North Sinai']
                   }
        if city != city:
            return 'nan'
        # check if city is in one of the values
        for key in regions:
            if city in regions[key]:
                return key
        self.logger.error(f'{city} not in regions')
        return 'nan'

    def clean_location(self, location: pd.Series) -> Tuple[pd.Series, pd.Series, pd.Series]:
        """
        cleans the location column

        Args:
            location (pd.Series): a location column

        returns:
            city (pd.Series): a city column
            governorate (pd.Series): a governorate column
            region (pd.Series): a region column
        Usage:
            df['city'], df['governorate'], df['region'] = clean_location(df['location'])
        """
        self.logger.info('Cleaning location column')
        cities = self.__get_governorates_cities(location)
        df_city = location.apply(lambda x: self.__get_city(x))
        df_governrate = location.apply(
            lambda x: self.__get_governorate(x, cities))
        df_region = df_governrate.apply(lambda x: self.__get_region(x))
        return df_city, df_governrate, df_region

    @staticmethod
    def __filter_digits(x: str) -> str:
        """
        Filters out digits from a string
        Args:
            x (str): a string

        Returns:
            str: a string without digits
        """
        if x != x:
            return x
        return re.sub(r'[^\d]', '', str(x))

    def __clean_bedroom(self, x: str) -> int:
        if '.html' in x:
            return 0
        return self.__filter_digits(x)

    def clean_bedrooms(self, bedrooms: pd.Series) -> pd.Series:
        """
        Cleans the bedrooms column

        Args:
            bedrooms (pd.Series): a bedrooms column

        Returns:
            pd.Series: a cleaned bedrooms column
        """
        self.logger.info('Cleaning bedrooms column')
        bedroom = bedrooms.apply(lambda x: self.__clean_bedroom(str(x)))
        return pd.to_numeric(bedroom, errors='coerce')

    def __clean_bathroom(self, x: str) -> int:
        return self.__filter_digits(x)

    def clean_bathrooms(self, bathrooms: pd.Series) -> pd.Series:
        """
        Cleans the bathrooms column

        Args:
            bathrooms (pd.Series): a bathrooms column

        Returns:
            pd.Series: a cleaned bathrooms column
        """
        self.logger.info('Cleaning bathrooms column')
        bathroom = bathrooms.apply(lambda x: self.__clean_bathroom(str(x)))
        return pd.to_numeric(bathroom, errors='coerce')

    def __clean_level(self, x: str) -> int:
        if 'Ground' in x:
            return 0
        if 'Highest' in x:
            return 10
        return self.__filter_digits(x)

    def clean_levels(self, levels: pd.Series) -> pd.Series:
        """
        Cleans the levels column

        Args:
            levels (pd.Series): a levels column

        Returns:
            pd.Series: a cleaned levels column
        """

        self.logger.info('Cleaning levels column')
        level = levels.apply(lambda x: self.__clean_level(x))
        pd.to_numeric(level, errors='coerce')

    def clean_area(self, area: pd.Series) -> pd.Series:
        """ Cleans the area column

        Args:
            area (pd.Series): The Area column

        Returns:
            pd.Series: The cleaned area column
        """
        self.logger.info('Cleaning area column')
        area = area.apply(lambda x: self.__filter_digits(x))
        return pd.to_numeric(area, errors='coerce')
