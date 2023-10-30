from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import Union
from bson.objectid import ObjectId as BsonObjectId


class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, ValidationInfo):
        if not isinstance(v, BsonObjectId):
            raise TypeError('ObjectId required')
        return str(v)
                            

class Weather(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    datetime: datetime
    epochtime: int
    temperature: Union[int, float] 
    weather_text: str


    @classmethod
    async def deserialize_external_data(cls, data):
        return Weather(
            datetime=data['LocalObservationDateTime'],
            epochtime=data['EpochTime'],
            weather_text=data['WeatherText'],
            temperature=data['Temperature']['Metric']['Value']
        )
