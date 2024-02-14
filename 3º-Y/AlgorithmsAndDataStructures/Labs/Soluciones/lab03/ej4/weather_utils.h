#include "weather.h"
#include "array_helpers.h"

#ifndef _WEATHER_UTILS_H
#define _WEATHER_UTILS_H
#define EXPECTED_WEATHER_FILE_FORMAT "%d %d %d %u %u %u"

//returns the minimum temperature of an array with temperatures.
int temp_min(WeatherTable data);

//returns the maximum temperature of an array with temperatures.
void max_temp(WeatherTable data, int output[YEARS]);

//returns the months of each year in which the amount of rainfall was the most.
void max_rainfall(WeatherTable data, month_t output[YEARS]);

#endif