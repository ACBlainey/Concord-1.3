import unittest
from g05_bta_distributed_control_087 import Restriction,audit

class DistributedTests(unittest.TestCase):
    def setUp(self):
        self.a=Restriction("M1","P1","C1",0,10,"ACCESS")
        self.b=Restriction("M2","P1","C2",10,20,"ACCESS")
    def check(self,items=None,union=15,concurrent=2):
        return audit([self.a,self.b] if items is None else items,"P1","ACCESS",0,30,union,concurrent)
    def test_distributed_continuity(self):self.assertEqual(self.check()["longest_continuous_ticks"],20)
    def test_union(self):self.assertEqual(self.check()["union_exposure_ticks"],20)
    def test_controllers(self):self.assertEqual(self.check()["contributing_controller_refs"],["C1","C2"])
    def test_exposure_flag(self):self.assertIn("DISTRIBUTED_EXPOSURE_REVIEW",self.check()["review_flags"])
    def test_adjacent_not_concurrent(self):self.assertEqual(self.check()["maximum_concurrent_controllers"],1)
    def test_overlap_concurrency(self):
        self.assertEqual(self.check([self.a,Restriction("M3","P1","C2",5,15)])["maximum_concurrent_controllers"],2)
    def test_concurrency_flag(self):
        self.assertIn("CONCURRENT_CONTROLLERS_REVIEW",self.check([self.a,Restriction("M3","P1","C2",5,15)])["review_flags"])
    def test_no_double_counting(self):
        self.assertEqual(self.check([self.a,Restriction("M3","P1","C2",5,15)])["union_exposure_ticks"],15)
    def test_same_controller_not_two(self):
        self.assertEqual(self.check([self.a,Restriction("M3","P1","C1",5,15)])["maximum_concurrent_controllers"],1)
    def test_other_subject_isolated(self):
        self.assertEqual(self.check([Restriction("M3","P2","C2",0,20)])["union_exposure_ticks"],0)
    def test_other_kind_isolated(self):
        self.assertEqual(self.check([Restriction("M3","P1","C2",0,20,"MOVEMENT")])["union_exposure_ticks"],0)
    def test_window_clip(self):
        self.assertEqual(audit([self.a],"P1","ACCESS",5,8,10,2)["union_exposure_ticks"],3)
    def test_no_authority(self):self.assertFalse(self.check()["authority_granted"])
    def test_no_illegality_inferred(self):self.assertFalse(self.check()["automatic_illegality"])
    def test_invalid_configuration(self):
        self.assertIn("INVALID_CONFIGURATION",audit([],"P1","ACCESS",5,5,1,2)["issues"])
    def test_duplicate_mandate(self):self.assertIn("DUPLICATE_MANDATE",self.check([self.a,self.a])["issues"])
    def test_invalid_interval(self):
        self.assertIn("INVALID_INTERVAL",self.check([Restriction("M3","P1","C1",10,9,"ACCESS")])["issues"])
    def test_below_threshold(self):self.assertFalse(self.check(union=21,concurrent=2)["review_required"])
if __name__=="__main__":unittest.main(verbosity=2)
