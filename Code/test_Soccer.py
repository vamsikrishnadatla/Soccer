import unittest
from Code import Soccer
import pandas as pd

data = pd.read_csv(r"C:\Users\vamsi.krishnadatla\Downloads\sc\soccer.csv")

class Soccertest(unittest.TestCase):

    def test_smallestdifference(self):
        result=(Soccer.smallestdifference(data))
        expected_results = " Leicester"
        self.assertEqual(result, expected_results)

    def test_Teamwithmostdraws(self):
        result_draws=(Soccer.Teamwithmostdraws(data))
        expected_draws = " Derby"
        self.assertEqual(result_draws, expected_draws)

    def test_Top10Teams(self):
        result_top10=(Soccer.Top10Teams(data))
        expected_top10 = pd.DataFrame(
            {'Team':['Arsenal', 'Liverpool', 'Manchester United', 'Newcastle', 'Leeds', 'Chelsea', 'West_Ham',
                      'Tottenham', 'Middlesbrough', 'Southampton']})
        expected_top10=expected_top10.to_string(index=False)
        self.assertEqual(result_top10, expected_top10)
