# validate_data.py
import pandas as pd
import pytest

# Assuming WeatherDataProcessor and FieldDataProcessor classes are defined elsewhere and imported here
from weather_data_processor import WeatherDataProcessor
from field_data_processor import FieldDataProcessor

# Load the data for testing
weather_df = pd.read_csv('sampled_weather_df.csv')
field_df = pd.read_csv('sampled_field_df.csv')

def test_read_weather_DataFrame_shape():
    """Test if the weather DataFrame has the expected shape."""
    assert weather_df.shape[0] > 0, "DataFrame is empty"
    assert weather_df.shape[1] > 0, "DataFrame has no columns"

def test_read_field_DataFrame_shape():
    """Test if the field DataFrame has the expected shape."""
    assert field_df.shape[0] > 0, "DataFrame is empty"
    assert field_df.shape[1] > 0, "DataFrame has no columns"

def test_weather_DataFrame_columns():
    """Test if the weather DataFrame contains expected columns."""
    expected_columns = ['Weather_station_ID', 'Message', 'Measurement', 'Value']  # Adjust columns as necessary
    assert all(column in weather_df.columns for column in expected_columns), "Missing one or more expected columns"

def test_field_DataFrame_columns():
    """Test if the field DataFrame contains expected columns."""
    expected_columns = ['Field_ID', 'Crop_type', 'Elevation', 'Rainfall']  # Adjust columns as necessary
    assert all(column in field_df.columns for column in expected_columns), "Missing one or more expected columns"

def test_field_DataFrame_non_negative_elevation():
    """Test if the Elevation values in field DataFrame are non-negative."""
    assert all(field_df['Elevation'] >= 0), "Negative elevation values found"

def test_crop_types_are_valid():
    """Test if Crop_type values in field DataFrame are valid, considering case sensitivity and whitespace."""
    valid_crop_types = ['cassava', 'tea', 'wheat', 'potato', 'banana', 'coffee', 'rice', 'maize']
    unique_crops = field_df['Crop_type'].str.lower().str.strip().unique()
    
    # Print all unique crop types for inspection
    print(f"Unique crop types found: {unique_crops}")

    invalid_crops = [crop for crop in unique_crops if crop not in valid_crop_types]
    assert not invalid_crops, f"Invalid crop types found: {invalid_crops}"

def test_positive_rainfall_values():
    """Test if all Rainfall values in field DataFrame are positive."""
    assert all(field_df['Rainfall'] > 0), "Non-positive rainfall values found"
