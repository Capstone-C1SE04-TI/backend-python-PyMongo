from mongoDB_init import client
import time

investorDocs = client['investors']

# investorDocs.update_many(
#     {},
#     {'$set' : {'TXs' : []}}
# )


investorDocs.update_many(
    {},
    {'$set' : {'coins' : {}}}
)
# investorAddresses = [investorDoc['_id'] for investorDoc in investorDocs.find({},{'TXs' : 0})]

# b = [1,2,3]
# for investorAddress,a in zip(investorAddresses,b):
#     print(investorAddress)
#     time.sleep(0.1)
