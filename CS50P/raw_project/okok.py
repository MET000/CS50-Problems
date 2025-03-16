


a = [{'a' : 'meto', 'b': 'mzwi', 'c': 'x'}, {'a' : 'ogh', 'b': 'bid', 'c': 'iui'}, {'a' : 'ghgh', 'b': 'kds', 'c': 'oqq'}]

gr = filter(lambda x: x['a'] == 'meto' , a)

for i in gr:

    print(i['c'])


app = [i['a'] for i in a if 'a']

print(app)



except requests.exceptions.ConnectionError:
        sys.exit(
            "Error: Unable to connect to the server. Please check your internet connection and try again."
        )
    except requests.exceptions.HTTPError as http_err:
        sys.exit(f"HTTP error occurred: {http_err}")
    except ValueError:
        sys.exit("Decoding JSON has failed")
    except TimeoutError:
        sys.exit()
    except RequestExceptionError:
        sys.exit()



except requests.exceptions.Timeout:
        sys.exit("The request timed out")
    except requests.exceptions.RequestException:
        sys.exit(
            "There was an ambiguous exception that occurred while handling your request"
        )
