import requests
import json
import os
from dotenv import load_dotenv
import csv


load_dotenv()

# endpoint = 'https://api.crunchbase.com/api/v4/autocompletes'
# headers = {
#     'accept': 'application/json',
#     "content-type": "application/json",
# }
#
# params = {
#     'query': 'Artificial Intelligence',
#     'collection_ids': 'category_groups,categories',
#     'limit': '25',
#     "user_key": os.environ.get("API_KEY"),
# }
#
# response = requests.get(endpoint, params=params, headers=headers)
#
# data = json.loads(response.text)
#
data = {'count': 9, 'entities': [{'identifier': {'entity_def_id': 'category', 'permalink': 'artificial-intelligence', 'uuid': 'c4d8caf3-5fe7-359b-f9f2-2d708378e4ee', 'value': 'Artificial Intelligence'}}, {'identifier': {'entity_def_id': 'category', 'permalink': 'intelligent-systems', 'uuid': '186d333a-99df-4a4a-6a0f-69bd2c0d0bba', 'value': 'Intelligent Systems'}}, {'identifier': {'entity_def_id': 'category', 'permalink': 'predictive-analytics-ca83', 'uuid': 'ca8390d7-22c6-5bb5-f870-22f52f364b1b', 'value': 'Predictive Analytics'}}, {'identifier': {'entity_def_id': 'category_group', 'permalink': 'artificial-intelligence-e551', 'uuid': 'e5514a50-8200-7f6b-de87-b07990670800', 'value': 'Artificial Intelligence'}}, {'identifier': {'entity_def_id': 'category', 'permalink': 'machine-learning', 'uuid': '5ea0cdb7-c9a6-47fc-50f8-c9b0fac04863', 'value': 'Machine Learning'}}, {'identifier': {'entity_def_id': 'category', 'permalink': 'natural-language-processing', 'uuid': '789bbbef-c46e-1532-a68d-f17da87090ea', 'value': 'Natural Language Processing'}}, {'identifier': {'entity_def_id': 'category_group', 'permalink': 'data-and-analytics', 'uuid': '701eef4f-18c1-4aff-b550-caf732cd575f', 'value': 'Data and Analytics'}}, {'identifier': {'entity_def_id': 'category_group', 'permalink': 'science-and-engineering', 'uuid': '285e29fc-8f70-bf00-1749-9e94158f64f4', 'value': 'Science and Engineering'}}, {'identifier': {'entity_def_id': 'category_group', 'permalink': 'software-85b6', 'uuid': '85b6bca9-930a-11bc-a608-a513b76fb637', 'value': 'Software'}, 'short_description': 'SaaS is Software.'}]}

# print(data)

data = data["entities"]
print(len(data))
category_group = []
for da in data:
    if da['identifier']['entity_def_id'] == 'category' and da['identifier']['permalink'] == 'artificial-intelligence':
        category_group.append(da['identifier']['uuid'])
#
# # open the file in the write mode
# # with open('output.csv', 'w', encoding='UTF8') as f:
# #     # create the csv writer
# #     writer = csv.writer(f)
# #
# #     # write a row to the csv file
# #     writer.writerow(data)
endpoint = "https://api.crunchbase.com/api/v4/searches/organizations"

headers = {
        "accept": "application/json",
        "content-type": "application/json",
        }

json_data = {
    'field_ids': [
        'identifier',
        'short_description',
        'num_founders',
        'founder_identifiers',
        'funds_total',
        'website_url',
        'valuation',
        'num_articles',
        'name'
    ],
    'order': [
        {
            'field_id': 'rank_org',
            'sort': 'asc',
        },
    ],
    'query': [
        {
            'type': 'predicate',
            'field_id': 'categories',
            'operator_id': 'includes',
            'values': category_group,
        },
    ]
}
params = {
    "user_key": os.environ.get("API_KEY")
}

# response = requests.post(endpoint, params=params, headers=headers, json=json_data)
#
# data = json.loads(response.text)
# print(data)
data = {'count': 30525, 'entities': [{'uuid': 'cf2c678c-b81a-80c3-10d1-9c5e76448e51', 'properties': {'name': 'OpenAI', 'identifier': {'permalink': 'openai', 'image_id': 'jjykwqqhsscreywea4gb', 'uuid': 'cf2c678c-b81a-80c3-10d1-9c5e76448e51', 'entity_def_id': 'organization', 'value': 'OpenAI'}, 'founder_identifiers': [{'permalink': 'elon-musk', 'image_id': 'hevy6dvk7gien0rmg37n', 'uuid': 'd3326bcc-6d25-9214-60c7-1e95c5f2f2a1', 'entity_def_id': 'person', 'value': 'Elon Musk'}, {'permalink': 'greg-brockman', 'image_id': 'n2dmdip1asycpbhphssy', 'uuid': '7fd3d201-18ea-fc1d-97ed-3daac3e9b8aa', 'entity_def_id': 'person', 'value': 'Greg Brockman'}, {'permalink': 'ilya-sutskever', 'image_id': 'v1484187041/ubonzlb6bz2reoceqxsg.png', 'uuid': '27e8c07e-41ef-03b3-9567-5c83a5fe2977', 'entity_def_id': 'person', 'value': 'Ilya Sutskever'}, {'permalink': 'john-schulman-950d', 'image_id': 'vka5n3zj1vdaxi9gulie', 'uuid': 'f18c757c-7466-4ff2-bff0-c4aa11f3950d', 'entity_def_id': 'person', 'value': 'John Schulman'}, {'permalink': 'sam-altman', 'image_id': 'eifaoe14zqiueje28oo9', 'uuid': 'f63055a5-a077-f7ad-2ace-9dbbac22a366', 'entity_def_id': 'person', 'value': 'Sam Altman'}, {'permalink': 'wojciech-zaremba', 'image_id': 'flg4p4evie7yjfwpc25a', 'uuid': '78995805-8abf-6e4c-8543-7877d29acbb4', 'entity_def_id': 'person', 'value': 'Wojciech Zaremba'}], 'short_description': 'OpenAI is an AI research and deployment company that conducts research and implements machine learning.', 'valuation': {'value_usd': 29000000000, 'currency': 'USD', 'value': 29000000000}, 'funds_total': {'value_usd': 100000000, 'currency': 'USD', 'value': 100000000}, 'num_articles': 1032, 'website_url': 'https://www.openai.com', 'num_founders': 6}}, {'uuid': '1e4f199c-363b-451b-a164-f94571075ee5', 'properties': {'name': 'Intel', 'identifier': {'permalink': 'intel', 'image_id': 'qpoiezeptj4q8krro55g', 'uuid': '1e4f199c-363b-451b-a164-f94571075ee5', 'entity_def_id': 'organization', 'value': 'Intel'}, 'founder_identifiers': [{'permalink': 'gordon-moore', 'image_id': 'v1491553922/bzpg2lb9zaybvkvqvloo.png', 'uuid': '41743958-4a4b-17a2-3360-dfc22f6a4ee3', 'entity_def_id': 'person', 'value': 'Gordon Moore'}, {'permalink': 'patrick-reilly-2', 'image_id': 'v1506029429/vd70xlvis7iuqmqlbuia.png', 'uuid': '0bb74943-c47a-6d3b-d466-bba73a3978a7', 'entity_def_id': 'person', 'value': 'Patrick Reilly'}, {'permalink': 'robert-noyce', 'image_id': 'v1491557238/feclvck6ejw8pnnkw0hi.png', 'uuid': '1fa8bfe0-ac19-1df0-2769-bbc35668a385', 'entity_def_id': 'person', 'value': 'Robert Noyce'}], 'short_description': 'Intel designs, manufactures, and sells integrated digital technology platforms worldwide.', 'num_articles': 36131, 'website_url': 'http://www.intel.com/', 'num_founders': 3}}, {'uuid': '6ff82ae5-eb70-42a2-83cd-20d17d61689b', 'properties': {'name': 'SandboxAQ', 'identifier': {'permalink': 'sandboxaq', 'image_id': 'u1gcptln74hc3zgyvws6', 'uuid': '6ff82ae5-eb70-42a2-83cd-20d17d61689b', 'entity_def_id': 'organization', 'value': 'SandboxAQ'}, 'short_description': 'SandboxAQ is an enterprise SaaS company that provides AI and quantum computing solutions.', 'num_articles': 21, 'website_url': 'https://www.sandboxaq.com'}}, {'uuid': 'e92c942f-e4f9-443f-bb1d-1ef2e93c50f8', 'properties': {'name': 'Cyble', 'identifier': {'permalink': 'cyble', 'image_id': 'cmilm6epfti9inztxdhb', 'uuid': 'e92c942f-e4f9-443f-bb1d-1ef2e93c50f8', 'entity_def_id': 'organization', 'value': 'Cyble'}, 'founder_identifiers': [{'permalink': 'beenu-arora', 'image_id': 'yfs4bjtkimfpcjnfgiwe', 'uuid': '47856edf-fc82-4633-8acf-5241f9503cac', 'entity_def_id': 'person', 'value': 'Beenu Arora'}, {'permalink': 'manish-chachda', 'image_id': 'x4nbgoetlf7zy0zkgtky', 'uuid': '1c962e97-8fa2-4ba5-8fbd-b502e900ec8e', 'entity_def_id': 'person', 'value': 'Manish Chachada'}], 'short_description': "World's fastest-growing threat intelligence provider (YC W21).", 'num_articles': 2205, 'website_url': 'https://cyble.com', 'num_founders': 2}}, {'uuid': '92b08fcb-61fd-40f2-8d1c-68dd2327c646', 'properties': {'name': 'Typeface', 'identifier': {'permalink': 'typeface', 'image_id': 's7i6r1b6xjq6md5werld', 'uuid': '92b08fcb-61fd-40f2-8d1c-68dd2327c646', 'entity_def_id': 'organization', 'value': 'Typeface'}, 'founder_identifiers': [{'permalink': 'abhay-parasnis', 'image_id': 'v1399304758/drbionk7pm1mdus7uryt.jpg', 'uuid': '0ee538e1-e0e4-a3c2-2d01-b76423a7e674', 'entity_def_id': 'person', 'value': 'Abhay Parasnis'}], 'short_description': 'Typeface is a generative AI application for creating enterprise content.', 'num_articles': 4, 'website_url': 'https://www.typeface.ai', 'num_founders': 1}}, {'uuid': 'ee17319e-f5ee-9c9a-6500-edf82b4fbf05', 'properties': {'name': 'NVIDIA', 'identifier': {'permalink': 'nvidia', 'image_id': 'v1502744943/jhowtgkdwv2aa1eodg2b.png', 'uuid': 'ee17319e-f5ee-9c9a-6500-edf82b4fbf05', 'entity_def_id': 'organization', 'value': 'NVIDIA'}, 'founder_identifiers': [{'permalink': 'chris-malachowsky', 'image_id': 'v1397185559/14923eb62b82d8ba1eb61d8a4f96e74e.jpg', 'uuid': '8bb21bf7-72f1-e57c-5665-8f64842a4a84', 'entity_def_id': 'person', 'value': 'Chris Malachowsky'}, {'permalink': 'curtis-priem', 'image_id': 'krpbwpg3fbgj0zblddem', 'uuid': 'f32c1c6b-2e43-4b9e-b0cc-76c5a8970ccc', 'entity_def_id': 'person', 'value': 'Curtis Priem'}, {'permalink': 'jen-hsun-huang', 'image_id': 'v1419917587/qpjgopqrtrak8ys4avgj.png', 'uuid': '8a189612-bd38-4dbe-241a-a7782d3ad0bc', 'entity_def_id': 'person', 'value': 'Jensen Huang'}], 'short_description': 'NVIDIA is a computing platform company operating at the intersection of graphics, HPC, and AI.', 'num_articles': 16907, 'website_url': 'https://www.nvidia.com', 'num_founders': 3}}, {'uuid': 'aef94694-259d-40be-9997-fa455a46da51', 'properties': {'name': 'Jasper', 'identifier': {'permalink': 'jasper-da51', 'image_id': 'oli64tx5zr9xncr0fypm', 'uuid': 'aef94694-259d-40be-9997-fa455a46da51', 'entity_def_id': 'organization', 'value': 'Jasper'}, 'founder_identifiers': [{'permalink': 'dave-rogenmoser', 'image_id': 'fwq9fpmy7yf8dbtgeiix', 'uuid': 'bf0c1c83-617b-aa27-794d-76c6758e6d29', 'entity_def_id': 'person', 'value': 'Dave Rogenmoser'}, {'permalink': 'john-philip-morgan-2', 'image_id': 'kebjdxuwehkbuopxnldu', 'uuid': 'a98d54f8-0b3f-ebff-d253-50d5527ad1e7', 'entity_def_id': 'person', 'value': 'John Philip Morgan'}], 'short_description': 'Jasper is an AI content platform that allows individuals and teams to use AI to scale their content strategies.', 'valuation': {'value_usd': 1500000000, 'currency': 'USD', 'value': 1500000000}, 'num_articles': 14, 'website_url': 'https://jasper.ai', 'num_founders': 2}}, {'uuid': 'bc56b253-f6f6-4b9c-b121-6c5493566e45', 'properties': {'name': 'Arloid Automation', 'identifier': {'permalink': 'arloid-automation', 'image_id': 'sy0ymwhu08f1n3fw391n', 'uuid': 'bc56b253-f6f6-4b9c-b121-6c5493566e45', 'entity_def_id': 'organization', 'value': 'Arloid Automation'}, 'founder_identifiers': [{'permalink': 'max-zubov', 'image_id': 'kkpcrw62a9ymfko1j2wx', 'uuid': '0eba938f-5c30-440b-ab23-f1cdf1606dac', 'entity_def_id': 'person', 'value': 'Max Zubov'}, {'permalink': 'sergey-shalunov', 'image_id': 'enewzupsvmpahstpfooc', 'uuid': '7cd5d68b-c847-4f28-b800-615d6163ed69', 'entity_def_id': 'person', 'value': 'Sergey Shalunov'}, {'permalink': 'vladimir-pushmin', 'image_id': 'qfus2it6y6dupmtos2gi', 'uuid': 'cd473b2d-bd5b-499f-876a-fa16f5e3d088', 'entity_def_id': 'person', 'value': 'Vladimir Pushmin'}], 'short_description': 'The ultimate AI solution for energy efficiency', 'num_articles': 371, 'website_url': 'https://arloid.com', 'num_founders': 3}}, {'uuid': 'e36f580e-6c0e-47de-accf-15de75f62cc9', 'properties': {'name': 'Stability AI', 'identifier': {'permalink': 'stability-ai', 'image_id': 'yaun2ev6hp27dz6lkhjv', 'uuid': 'e36f580e-6c0e-47de-accf-15de75f62cc9', 'entity_def_id': 'organization', 'value': 'Stability AI'}, 'founder_identifiers': [{'permalink': 'cyrus-christophe-hodes', 'image_id': 'tn37ee5z3lajjatsqgbd', 'uuid': '1bb20a43-eafa-4c53-9c99-77aa4c6362cf', 'entity_def_id': 'person', 'value': 'Cyrus Hodes'}, {'permalink': 'emad-mostaque', 'image_id': 'kavcwjrjvzudj9k24oam', 'uuid': 'b690d00b-2391-4b84-939c-333e75996589', 'entity_def_id': 'person', 'value': 'Emad Mostaque'}], 'short_description': 'Stability AI is an AI-driven visual art startup that designs and implements an open AI tool to create images based on text input given.', 'valuation': {'value_usd': 1000000000, 'currency': 'USD', 'value': 1000000000}, 'num_articles': 31, 'website_url': 'https://www.stability.ai', 'num_founders': 2}}, {'uuid': '54814919-9a8d-497b-bf71-90a23f744c98', 'properties': {'name': 'Una Brands', 'identifier': {'permalink': 'una-brands', 'image_id': 'waq86cut8lkirj3l5d9u', 'uuid': '54814919-9a8d-497b-bf71-90a23f744c98', 'entity_def_id': 'organization', 'value': 'Una Brands'}, 'founder_identifiers': [{'permalink': 'adrian-johnston', 'image_id': 'w6h5vjuivmucvbvfbrgq', 'uuid': 'd6249edb-5e09-49d9-8c85-d990c47e31be', 'entity_def_id': 'person', 'value': 'Adrian Johnston'}, {'permalink': 'kiren-tanna', 'image_id': 'v1414066339/c5b4jzytklximojbqugc.jpg', 'uuid': '6e1b29e7-ff04-1daa-71da-093901414da9', 'entity_def_id': 'person', 'value': 'Kiren Tanna'}, {'entity_def_id': 'person', 'permalink': 'kushal-patel-869a', 'uuid': 'aadf93c4-cbed-493a-811c-cd16bc9f869a', 'value': 'Kushal Patel'}, {'entity_def_id': 'person', 'permalink': 'srinivasan-shridharan', 'uuid': '29250157-8515-4f14-b68e-fa5c66100af6', 'value': 'Srinivasan Shridharan'}, {'entity_def_id': 'person', 'permalink': 'tobias-heusch', 'uuid': '3dbd649c-a1d2-49bf-9d44-fc2a3f0ba629', 'value': 'Tobias Heusch'}], 'short_description': 'Una Brands provides a streamlined way for e-commerce business owners to sell their companies.', 'num_articles': 25, 'website_url': 'https://www.una-brands.com', 'num_founders': 5}}]}

data = data["entities"]
print(len(data))
final_data = []
for da in data:
    # print(da.keys())
    d = da['properties']
    # print(d)
    print(type(d))
    # fields_name = d.keys()
    # file_name = f"{d.get('name')}.csv"
    list = []
    list.append(d)
    founders = []
    if d.get('founder_identifiers') is None:
        pass
    else:
        for a in d.get('founder_identifiers'):
            founders.append(a.get('value'))
    # print(founders)
    print(f"Company Name:{d.get('name')}")
    print(f"Short Description: {d.get('short_description')}")
    print(f"Founders: {founders}")
    print(f"Valuation: {d.get('valuation')}")
    print(f"Funds Total: {d.get('funds_total')}")
    print(f"Number of Articles: {d.get('num_articles')}")
    print(f"Website: {d.get('website_url')}")
    print(f"Number of Founders: {d.get('num_founders')}")
    print("\n")
    result = {
        'Company Name': d.get('name'),
        'short description': d.get('short_description'),
        'num of founders': d.get('num_founders'),
        'founders': founders,
        'funds total': d.get('funds_total'),
        'website url': d.get('website_url'),
        'valuation': d.get('valuation'),
        'num of articles': d.get('num_articles'),
    }
    final_data.append(result)

fieldnames = ['Company Name', 'short description', 'num of founders', 'founders', 'funds total', 'website url', 'valuation', 'num of articles']
with open('output.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(final_data)