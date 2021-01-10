import requests
from flask_restful import Resource, reqparse
from A2.models.user import UserModel
from A2.bar_chart import BarChart


class CovidData(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help="This field cannot remain empty")
    parser.add_argument('country', type=str, required=False)
    parser.add_argument('days', type=int, required=False)

    def post(self):
        data = CovidData.parser.parse_args()
        if UserModel.find_by_email(data['email']):

            # url = https://corona.lmao.ninja/v2/historical/:query?lastdays=30 - 'GET'
            endpoint = "https://corona.lmao.ninja/v2/historical/"
            if data['country'] and data['days']:
                response = requests.get(f"{endpoint}{data['country']}?lastdays={data['days']}")
            else:  # default option
                default_country = UserModel.fetch_country_by_email(data['email'])
                response = requests.get(f"{endpoint}{default_country}?lastdays=15")

            json_response = response.json()
            BarChart.bar_chart(json_response['timeline']['cases'])
            return response.json()
        else:
            return {'message': "User with email id {} is not yet signed up".format(data['email'])}