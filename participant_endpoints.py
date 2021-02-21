import requests
import json

PARTICIPANTS_INDEX_URL = 'https://data.directory.openbankingbrasil.org.br/participants'
ENDPOINT_MARKER = '/open-banking'
response = requests.get(PARTICIPANTS_INDEX_URL)
participants = json.loads(response.text)


def get_particpant_name(participant):
    return participant['OrganisationName']


def get_endpoint(participant):
    endpoint = participant['AuthorisationServers'][0]['ApiResources'][0]['ApiDiscoveryEndpoints'][0]['ApiEndpoint']
    marker_index = endpoint.index(ENDPOINT_MARKER) + len(ENDPOINT_MARKER)
    return endpoint[:marker_index]


def get_endpoints():
    endpoints = dict()

    for participant in participants:
        try:
            name = get_particpant_name(participant)
            endpoint = get_endpoint(participant)
            endpoints[name] = endpoint
        except IndexError:
            # participant does not have this resource. Just skip it.
            pass
    return endpoints
