import unittest
from g05_gtp_resource_collision_076 import Claim,assess,can_execute

class CollisionTests(unittest.TestCase):
    def setUp(self):
        self.a=Claim("A1","GTP-A","OWNER-A","PUMP-1",4,"MANDATE-A","EXCLUSIVE","ACTIVE")
        self.b=Claim("B1","GTP-B","OWNER-B","PUMP-1",7,"MANDATE-B","EXCLUSIVE","ACTIVE")
    def test_conflict_detected(self):self.assertIn("CROSS_AREA_RESOURCE_COLLISION:PUMP-1",assess([self.a,self.b])["issues"])
    def test_no_automatic_winner(self):self.assertIsNone(assess([self.a,self.b])["automatic_winner"])
    def test_both_blocked(self):
        self.assertFalse(can_execute(self.a,[self.a,self.b],True))
        self.assertFalse(can_execute(self.b,[self.a,self.b],True))
    def test_owner_attestation_not_enough(self):self.assertFalse(can_execute(self.a,[self.a,self.b],True))
    def test_expired_other_claim(self):
        b=Claim("B1","GTP-B","OWNER-B","PUMP-1",7,"MANDATE-B","EXCLUSIVE","EXPIRED")
        self.assertTrue(can_execute(self.a,[self.a,b],True))
    def test_different_resources(self):
        b=Claim("B1","GTP-B","OWNER-B","PUMP-2",7,"MANDATE-B","EXCLUSIVE","ACTIVE")
        self.assertTrue(can_execute(self.a,[self.a,b],True))
    def test_shared_modes(self):
        a=Claim("A1","GTP-A","OWNER-A","PUMP-1",4,"MANDATE-A","SHARED","ACTIVE")
        b=Claim("B1","GTP-B","OWNER-B","PUMP-1",7,"MANDATE-B","SHARED","ACTIVE")
        self.assertFalse(assess([a,b])["issues"])
    def test_mixed_mode_collision(self):
        b=Claim("B1","GTP-B","OWNER-B","PUMP-1",7,"MANDATE-B","SHARED","ACTIVE")
        self.assertTrue(assess([self.a,b])["issues"])
    def test_missing_mandate(self):
        a=Claim("A1","GTP-A","OWNER-A","PUMP-1",4,"","EXCLUSIVE","ACTIVE")
        self.assertIn("INVALID_MANDATE_REFERENCE",assess([a])["issues"])
    def test_duplicate_id(self):self.assertIn("DUPLICATE_CLAIM_ID",assess([self.a,self.a])["issues"])
    def test_no_attestation(self):self.assertFalse(can_execute(self.a,[self.a],False))
    def test_no_parent_child_authority(self):
        b=Claim("B1","GTP-A-CHILD","OWNER-B","PUMP-1",7,"MANDATE-B","EXCLUSIVE","ACTIVE")
        self.assertTrue(assess([self.a,b])["requires_owner_reconciliation"])
if __name__=="__main__":unittest.main(verbosity=2)
