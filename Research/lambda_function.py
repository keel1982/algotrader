import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps([{'ticker': 'FB', 'reason': 'Facebook good adverticement company'},
                            {'ticker': 'SEDG', 'reason': 'SolarEdge-green energie'},
                            {'ticker': 'LTHM', 'reason': 'Livent-lithium batteries- used even with Tesla'},
                            {'ticker': 'SQ', 'reason': 'Square, Inc. provides, together with its subsidiaries, payment and point-of-sale solutions in the United States and internationally.'},
                            {'ticker': 'TTWO', 'reason': 'Take-Two Interactive Software, Inc. develops, publishes, and markets interactive entertainment solutions for consumers worldwide.'},
                            {'ticker': 'OTRK', 'reason': 'Ontrak, Inc. operates as an artificial intelligence powered, virtualized outpatient healthcare treatment company that provides in-person or telehealth intervention services to health plans and other third-party payors'},
                            {'ticker': 'HUM', 'reason': 'Humana Inc., together with its subsidiaries, operates as a health and well-being company in the United States.'},
                            {'ticker': 'AAPL', 'reason': 'Apple- as we love it'},
                            {'ticker': 'ZG', 'reason': 'Zillow Group, Inc. operates real estate brands on mobile and the web in the United States'},
                            {'ticker': 'MSFT', 'reason': 'Microsoft- as we know and love of what it does for Enterprize'},
                            {'ticker': 'NVDA', 'reason': 'Nvidia- because of AI part and gpu needed for bitcoins'},
                            {'ticker': 'BEP', 'reason': 'Brookfield Renewable Partners L.P. owns a portfolio of renewable power generating facilities, but also doing real bussiness of garbage'},
                            {'ticker': 'GOOGL', 'reason': 'Google- her majesty'},
                            {'ticker': 'ETSY', 'reason': 'Etsy- as online shopping platform fast growing'},
                            {'ticker': 'IVAC', 'reason': 'Intevac, Inc. provides vacuum deposition equipment for various thin-film applications, and digital night-vision technologies and products to the defense industry in the United States'},
                            {'ticker': 'PTON', 'reason': 'Pelaton - because of marketing and because it offers platform and sport gamification- for quarantine'},
                            {'ticker': 'ADI', 'reason': 'Analog Devices, Inc. designs, manufactures, and markets integrated circuits (ICs)'},
                            {'ticker': 'CRM', 'reason': 'salesforce.com, inc. develops enterprise cloud computing solutions with a focus on customer relationship management worldwide'},
                            {'ticker': 'CHWY', 'reason': 'Chewy, Inc., provides ecomerce for pets'},
                            {'ticker': 'AZN', 'reason': 'AstraZeneca PLC discovers, develops, and commercializes prescription medicines in the areas of oncology, cardiovascular, renal and metabolism, respiratory, autoimmunity, infection, neuroscience, and gastroenterology worldwide'}])
    }
