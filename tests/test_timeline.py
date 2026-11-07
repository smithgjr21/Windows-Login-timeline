import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from login_timeline import analyze
class LoginTests(unittest.TestCase):
 def test_repeated_failures(self):
  result=analyze(Path(__file__).resolve().parents[1]/'samples/security_events.csv')
  self.assertEqual(len(result['timeline']),5)
  self.assertEqual(result['repeated_failures'][0]['failed_login_count'],3)
if __name__=='__main__':unittest.main()
