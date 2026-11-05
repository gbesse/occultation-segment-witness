import unittest,math
from occultation_segment_witness.core import run
class DomainTests(unittest.TestCase):
 def test_crossing(self):
  x=run({'start':[-2,0,0],'end':[2,0,0],'radius':1});self.assertEqual(x['intersection_fractions'],[.25,.75]);self.assertTrue(x['blocked'])
 def test_ray_not_segment(self):self.assertFalse(run({'start':[2,0,0],'end':[3,0,0],'radius':1})['blocked'])
 def test_tangent(self):self.assertEqual(run({'start':[-2,1,0],'end':[2,1,0],'radius':1})['clearance'],0)
 def test_point(self):self.assertTrue(run({'start':[0,0,0],'end':[0,0,0],'radius':1})['blocked'])
