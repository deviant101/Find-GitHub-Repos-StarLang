import requests
from functional_logic.models import GitHubRepo
from functional_logic.exceptions import GitHubApiException

GH_SEARCH_API_URL = "https://api.github.com/search/repositories"

def most_stars_repos(languages, min_stars=100000, sort="stars", order="ascending"):

    query = create_query(languages=languages, min_stars=min_stars)
    parameters = {"q":query, "sort":sort, "order":order}
    response = requests.get(GH_SEARCH_API_URL,params=parameters)
    
    if response.status_code != 200:
        raise GitHubApiException(response.status_code)

    json_response = response.json()
    # print(json_response["items"][0].keys())   # to filter & find useful keys of repo
    items = json_response["items"]              # returning list of dictionaries

    return [GitHubRepo(item["name"], item["language"], item["stargazers_count"]) for item in items]

def create_query(languages, min_stars):
    
    query = " ".join( f"language:{lang}" for lang in languages )
    query += f" stars:>{min_stars}"
    return query

def main():
    languages = ["Python", "JavaScript", "Typescript"]
    # print(most_stars_repos(languages=languages))
    for repo in most_stars_repos(languages=languages):
        print(f"-> {repo}")


if __name__ == "__main__":
    main()