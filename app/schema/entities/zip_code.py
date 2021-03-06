from mara_schema.entity import Entity
from mara_schema.attribute import Type

zip_code_entity = Entity(
    name='Zip code',
    description='Information on Brazilian zip codes including coordinates',
    schema_name='ec_dim',
    table_name='zip_code'
)

zip_code_entity.add_attribute(
    name='Zip code ID',
    description='Unique identifier of a geo-location entry based on the zip code',
    column_name='zip_code_id',
    type=Type.ID)

zip_code_entity.add_attribute(
    name='Zip code',
    description='First 5 digits of the zip code (Brazil has an 8-digit system)',
    column_name='zip_code')

zip_code_entity.add_attribute(
    name='Latitude',
    description='Latitude coordinate',
    column_name='latitude')

zip_code_entity.add_attribute(
    name='Longitude',
    description='Longitude coordinate',
    column_name='longitude')

zip_code_entity.add_attribute(
    name='City',
    description='City name',
    column_name='city',
    important_field=True)

zip_code_entity.add_attribute(
    name='State',
    description='State name',
    column_name='state')
