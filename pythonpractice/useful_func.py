def get_10(data):
    sorted_data=sorted(data,key=lambda key:key['population'],reverse=True)
    top_10=sorted_data[:10]
    return [f"{i['name']}:-{','.join(i['languages'])}"for i in top_10]