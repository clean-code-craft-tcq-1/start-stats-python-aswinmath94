import unittest
import statistics
import math

class EmailAlert():
  def __init__(self):
    self.emailSent = 1


class LEDAlert():
  def __init__(self):
    self.ledGlows = 1

class StatsAlerter():

  def __init__(self, threshold, alerts):
    self.threshold = threshold
    self.emailSent = alerts[0]
    self.ledGlows = alerts[1]

  def checkAndAlert(self,number_list):
    max_num = max(number_list)
    if max_num > self.threshold:
      self.emailSent = 1
      self.ledGlows = 1
      EmailAlert.emailSent = 1
      LEDAlert.ledGlows = 1


class StatsTest(unittest.TestCase):

  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525,delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    check = math.isnan(float(computedStats["avg"])) and math.isnan(float(computedStats["max"])) and math.isnan(float(computedStats["min"]))
    self.assertTrue(check)



  def test_raise_alerts_when_max_above_threshold(self):
    emailAlert = EmailAlert()
    ledAlert = LEDAlert()
    maxThreshold = 10.5
    statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
    statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
    self.assertTrue(emailAlert.emailSent)
    self.assertTrue(ledAlert.ledGlows)



if __name__ == "__main__":
  unittest.main()
