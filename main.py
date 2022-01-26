import io
import psycopg2
import pandas as pd

cobranca_pacientes = pd.read_csv(r'Datasets\inpatientCharges.csv')
cobranca_pacientes[' Average Covered Charges '] = cobranca_pacientes[' Average Covered Charges '].str.replace('$','')
cobranca_pacientes[' Average Total Payments '] = cobranca_pacientes[' Average Total Payments '].str.replace('$','')
cobranca_pacientes['Average Medicare Payments'] = cobranca_pacientes['Average Medicare Payments'].str.replace('$','')

diagnosticos = pd.read_csv(r'Datasets\datasets_180_408_data.csv')
diagnosticos.drop(diagnosticos.columns[len(diagnosticos.columns)-1], axis=1, inplace=True)