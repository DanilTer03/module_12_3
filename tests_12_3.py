import unittest
from rt_with_exceptions import Tournament, Runner


def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            print(f'Тесты в {self.__class__.__name__} заморожены.')
            return
        return func(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("John Doe", 10)
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Jane Doe", 10)
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner 1", 10)
        runner2 = Runner("Runner 2", 9)
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)



class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @skip_if_frozen
    def test_race_usain_nik(self):
        tournament = Tournament(90)
        tournament.add_runner(self.usain)
        tournament.add_runner(self.nik)
        results = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results)] = results
        last_runner = max(TournamentTest.all_results.keys())
        self.assertTrue("Ник" in results and results[last_runner] == self.nik.distance)

    @skip_if_frozen
    def test_race_andrei_nik(self):
        tournament = Tournament(90)
        tournament.add_runner(self.andrei)
        tournament.add_runner(self.nik)
        results = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results)] = results
        last_runner = max(TournamentTest.all_results.keys())
        self.assertTrue("Ник" in results and results[last_runner] == self.nik.distance)

    @skip_if_frozen
    def test_race_usain_andrei_nik(self):
        tournament = Tournament(90)
        tournament.add_runner(self.usain)
        tournament.add_runner(self.andrei)
        tournament.add_runner(self.nik)
        results = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results)] = results
        last_runner = max(TournamentTest.all_results.keys())
        self.assertTrue("Ник" in results and results[last_runner] == self.nik.distance)