#include "weather.h"
#include "array_helpers.h"

int temp_min(WeatherTable data){
    unsigned int year,day;
    month_t month;
    int min=data[0][january][0]._min_temp;
    

    for(year=0;year<YEARS;year++){
        for(month=january;month<=december;month++){
            for(day=0;day<LST_DAY;day++){
                if(min>data[year][month][day]._min_temp){
                    min=data[year][month][day]._min_temp;
                }
            }
        }
    }
    
    return min; 
}


void max_temp(WeatherTable data, int output[YEARS]){
    unsigned int year,day;
    int max;
    month_t month;
    
    for(year=0;year<YEARS;year++){
        max=data[year][january][FST_DAY]._max_temp;
        for(month=january;month<=december;month++){
            for(day=0;day<LST_DAY;day++){
                if(max<data[year][month][day]._max_temp){
                max=data[year][month][day]._max_temp;
                }
            }
        }
        output[year]=max;
    }
}

void max_rainfall(WeatherTable data, month_t output[YEARS]){
    unsigned int year,day,max_rainf,rainf;
    month_t month, max_month;

    for(year=0;year<YEARS;year++){
        max_month=january;
        max_rainf=0;      
        for(month=january;month<=december;month++){
            rainf=0;
            for(day=0;day<LST_DAY;day++){
                rainf+=data[year][month][day]._rainfall;
            }
            if(rainf>max_rainf){
                max_rainf=rainf;
                max_month=month;
            }
        }
        output[year]=max_month;
    }
}