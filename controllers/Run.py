from datetime import datetime

import controllers.menu_controllers
from controllers.match_controllers import MatchController
from controllers.round_controllers import RoundController
from controllers.tournamenent_controllers import TournamentController
from models.match import Match
from models.round import Round
from models.tournament import Tournament


class RunCreationTournoi:
    """
    This controller is responsible for creating a new tournament:
    -add info tournament
    -add players tournament
    save players and tournaments in json files
    """

    def __init__(self):
        self.tournament = Tournament(None, None, None, None)

    def __call__(self, *args, **kwargs):
        controller_tournoi = TournamentController(self.tournament)
        controller_tournoi.creation_tournoi()
        controller_tournoi.input_number_players_controller()
        controller_tournoi.save_tournament_info_to_json_controller()
        controller_tournoi.save_player_tournament_to_json_controller()

        run_instance = Run(self.tournament)
        run_instance()


class Run:
    """
    Controller for running tournament rounds and managing matches.
    This controller is responsible for running the rounds of a tournament, managing match pairings,
    and updating scores.
    """

    def __init__(self, tournament):
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        controller_tournoi = TournamentController(self.tournament)

        controller_tournoi.display_tournament_info_controller()
        controller_tournoi.display_player_tournament_controller()

        for tour in range(
            self.tournament.get_numbers_round() - self.tournament.get_actual_round()
        ):
            controller_tournoi.sort_players_by_score_controller()

            controller_tournoi.increment_actual_round_controller()
            controller_tournoi.display_actual_numero_round_controller()

            round_tournament = Round(
                name="Round " + controller_tournoi.get_name_controller()
            )
            controller_round = RoundController(round_tournament)
            controller_round.set_numero_controller(
                controller_tournoi.get_actual_round_controller()
            )
            controller_round.set_date_save_controller(datetime.now().isoformat())

            app = controllers.menu_controllers.ApplicationController()
            app.choixjouerleround(round_tournament)

            creation_pair_match_instance = CreationPairMatch(
                self.tournament, round_tournament
            )
            creation_pair_match_instance()

            continuer_round_instance = AskContinuerRoundRun(round_tournament)
            continuer_round_instance()

            controller_tournoi.add_list_tournament_round_controller(round_tournament)

            score_instance = UpdateScoreRun(self.tournament, round_tournament)
            score_instance()

            controller_tournoi.score_player_tournament_controller()

            controller_round.save_round_to_json_controller()
            controller_round.save_match_round_to_json_controller()
            controller_tournoi.save_round_tournament_to_json_controller()

        controller_tournoi.display_end_tournament_controller()
        app = controllers.menu_controllers.ApplicationController()
        app.start()


class AskContinuerRoundRun:
    def __init__(self, round_game):
        self.round = round_game

    def __call__(self, *args, **kwargs):
        controller_round = RoundController(self.round)

        for match in controller_round.get_match_controller():
            controller_match = MatchController(match)
            controller_match.display_match_controller()
            app = controllers.menu_controllers.ApplicationController()
            app.choixgagnantmatch(match)
            controller_match.save_match_to_json_controller()


class UpdateScoreRun:
    """
    Update player scores based on match results in the current round.
    This method iterates through the matches in the current round and updates the scores of players in the
    tournament accordingly.
    """

    def __init__(self, tournament, round_game):
        self.tournament = tournament
        self.round = round_game

    def __call__(self, *args, **kwargs):
        controller_round = RoundController(self.round)
        contoller_tournament = TournamentController(self.tournament)

        for match in controller_round.get_match_controller():
            for players in contoller_tournament.get_tournament_players_controller():
                if match.player1.name == players.name:
                    players.score += match.score1
                if match.player2.name == players.name:
                    players.score += match.score2


class CreationPairMatch:
    """
    Create match pairings in the current round of the tournament.
    This method generates fair match pairings in the current round, taking into account the players' previous
    pairings in previous rounds.
    """

    def __init__(self, tournament, round_game):
        self.tournament = tournament
        self.round = round_game

    def __call__(self, *args, **kwargs):
        controller_round = RoundController(self.round)
        contoller_tournament = TournamentController(self.tournament)

        pairs_history = []
        for round_game in contoller_tournament.get_list_rounds_controller():
            for match in round_game.matchs:
                pairs_history.append((match.player1, match.player2))

        remaining_players = contoller_tournament.get_remaining_players_controllers()

        while len(remaining_players) >= 2:
            player1 = remaining_players.pop(0)
            player2 = None
            for other_player in remaining_players:
                if (player1, other_player) not in pairs_history and (
                    other_player,
                    player1,
                ) not in pairs_history:
                    player2 = other_player
                    remaining_players.remove(player2)
                    new_match = Match(
                        player1, player2, date_save=datetime.now().isoformat()
                    )
                    new_match.random_color()
                    controller_round.add_match_controller(new_match)
                    pairs_history.append((player1, player2))
                    break
            if player2 is None:
                player2 = remaining_players.pop(0)
                new_match = Match(
                    player1, player2, date_save=datetime.now().isoformat()
                )
                new_match.random_color()
                controller_round.add_match_controller(new_match)
                pairs_history.append((player1, player2))

        controller_round.display_match_players_controller()
