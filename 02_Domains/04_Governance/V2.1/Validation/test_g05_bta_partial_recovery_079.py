import unittest
from g05_bta_partial_recovery_079 import Transition

class RecoveryTests(unittest.TestCase):
    def setUp(self):self.t=Transition("TX1")
    def test_initial_state(self):self.assertEqual(self.t.state,"APPROVED_NOT_EXECUTED")
    def test_no_start_without_revalidation(self):self.assertFalse(self.t.start(False))
    def test_start(self):self.assertTrue(self.t.start(True))
    def test_successful_step(self):
        self.t.start(True);self.assertTrue(self.t.step("A",True));self.assertEqual(self.t.completed_steps,["A"])
    def test_failed_step_preserves_history(self):
        self.t.start(True);self.t.step("A",True);self.t.step("B",False)
        self.assertEqual(self.t.completed_steps,["A"]);self.assertEqual(self.t.failed_steps,["B"])
    def test_failure_surviving_duty(self):
        self.t.start(True);self.t.step("B",False)
        self.assertIn("RECOVERY_ASSESSMENT",self.t.surviving_duties)
    def test_no_step_after_failure(self):
        self.t.start(True);self.t.step("B",False);self.assertFalse(self.t.step("C",True))
    def test_interruption_preserves_reason(self):
        self.t.start(True);self.t.interrupt("power loss")
        self.assertIn("INTERRUPTION:power loss",self.t.failed_steps)
    def test_recovery_requires_owner(self):
        self.t.start(True);self.t.interrupt("network")
        self.assertFalse(self.t.propose_recovery(False,True))
    def test_recovery_requires_fresh_dependencies(self):
        self.t.start(True);self.t.interrupt("network")
        self.assertFalse(self.t.propose_recovery(True,False))
    def test_recovery_does_not_restore_automatically(self):
        self.t.start(True);self.t.interrupt("network");self.t.propose_recovery(True,True)
        self.assertEqual(self.t.state,"RECOVERY_PENDING")
    def test_recovery_requires_evidence(self):
        self.t.start(True);self.t.interrupt("network");self.t.propose_recovery(True,True)
        self.assertFalse(self.t.record_recovery(""))
    def test_failure_blocks_false_completion(self):
        self.t.start(True);self.t.step("B",False);self.t.propose_recovery(True,True);self.t.record_recovery("EV")
        self.assertFalse(self.t.conclude(True,True))
    def test_completion_requires_owner(self):
        self.t.start(True);self.t.step("A",True)
        self.assertFalse(self.t.conclude(False,True))
    def test_completion_requires_duties_resolved(self):
        self.t.start(True);self.t.step("A",True)
        self.assertFalse(self.t.conclude(True,False))
    def test_normal_completion(self):
        self.t.start(True);self.t.step("A",True)
        self.assertTrue(self.t.conclude(True,True))
        self.assertFalse(self.t.authority_granted)
if __name__=="__main__":unittest.main(verbosity=2)
