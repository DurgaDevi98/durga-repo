import re


story = "my name is durga, and I work in hallmark at kakinada city. kakinada is a city in andhra pradesh. its famous for a sweet called kaja. kaja is sold at the every street of kakinada."


person = {
    "name": "durga",
    "company": "hallmark",
    "city": "kakinada",
    "favorite": "kaja",
}


extracted_entities = []


for key, value in person.items():
    for match in re.finditer(value, story, re.IGNORECASE):
        start_index = match.start()
        end_index = match.end()
        matched_value = match.group()
        extracted_entities.append({
            "start": start_index,
            "end": end_index,
            "value": matched_value,
            "entity": key
        })

print("Extracted entities:", extracted_entities)