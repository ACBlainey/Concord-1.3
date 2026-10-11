import unittest
from g05_bta_cumulative_control_086 import Intervention,exposure

class CumulativeTests(unittest.TestCase):
    def setUp(self):
        self.a=Intervention("M1","P1","C1",0,10)
        self.b=Intervention("M2","P1","C1",10,20)
    def check(self,items=None,total=15,continuous=15):
        return exposure([self.a,self.b] if items is None else items,"P1","C1",0,30,total,continuous)
    def test_adjacent_merge(self):self.assertEqual(self.check()["merged_intervals"],[(0,20)])
    def test_total(self):self.assertEqual(self.check()["total_exposure_ticks"],20)
    def test_longest(self):self.assertEqual(self.check()["longest_continuous_ticks"],20)
    def test_cumulative_flag(self):self.assertIn("CUMULATIVE_EXPOSURE_REVIEW",self.check()["review_flags"])
    def test_continuous_flag(self):self.assertIn("CONTINUOUS_CONTROL_REVIEW",self.check()["review_flags"])
    def test_no_auto_illegality(self):self.assertFalse(self.check()["automatic_illegality"])
    def test_no_authority(self):self.assertFalse(self.check()["authority_granted"])
    def test_overlap_not_double_counted(self):
        self.assertEqual(self.check([self.a,Intervention("M3","P1","C1",5,15)])["total_exposure_ticks"],15)
    def test_gap_separates(self):
        result=self.check([self.a,Intervention("M3","P1","C1",12,20)])
        self.assertEqual(result["longest_continuous_ticks"],10)
    def test_other_controller_isolated(self):
        self.assertEqual(self.check([Intervention("M4","P1","C2",0,20)])["total_exposure_ticks"],0)
    def test_other_subject_isolated(self):
        self.assertEqual(self.check([Intervention("M4","P2","C1",0,20)])["total_exposure_ticks"],0)
    def test_window_clipping(self):
        self.assertEqual(exposure([self.a],"P1","C1",5,8,100,100)["total_exposure_ticks"],3)
    def test_no_records(self):self.assertFalse(self.check([])["requires_independent_review"])
    def test_duplicate_ref(self):
        self.assertIn("DUPLICATE_MANDATE_REF",self.check([self.a,self.a])["issues"])
    def test_invalid_interval(self):
        self.assertIn("INVALID_INTERVAL",self.check([Intervention("X","P1","C1",8,3)])["issues"])
    def test_invalid_configuration(self):
        self.assertIn("INVALID_CONFIGURATION",exposure([],"P1","C1",10,10,1,1)["issues"])
    def test_below_threshold(self):self.assertFalse(self.check(total=21,continuous=21)["requires_independent_review"])
    def test_continuous_only(self):
        self.assertEqual(self.check(total=21,continuous=15)["review_flags"],["CONTINUOUS_CONTROL_REVIEW"])
if __name__=="__main__":unittest.main(verbosity=2)
