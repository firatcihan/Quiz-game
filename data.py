import requests
question_data = []
parametreler = {
    "amount": 40,
    "category": 15,
    "type": "boolean"
}
cevap = requests.get(url="https://opentdb.com/api.php" , params=parametreler)
cevap.raise_for_status()
sorular = cevap.json()

for soru in sorular["results"]:
    question_data.append(soru)    
print(len(question_data))

