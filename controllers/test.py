for tour in range(self.tournament.get_numbers_round() - self.tournament.get_actual_round()):
    controller_tournoi.sort_players_by_score_controller()
    controller_tournoi.display_actual_numero_round_controller()
    controller_tournoi.increment_actual_round_controller()

    round_tournament = Round()
    controller_round = RoundController(round_tournament)
    controller_round.increment_numero_round_controller()
    controller_round.set_commence_controller(datetime.now().isoformat())

    #           pair history

    pairs_history = []

    for round in self.tournament.list_round:
        for match in round.matchs:
            pairs_history.append((match.player1, match.player2))

    print(pairs_history)

    #                    code tournoi
    print(controller_tournoi.nombre_de_participants_controller())
    if controller_tournoi.nombre_de_participant_pair_controller():
        # Liste des joueurs restants
        remaining_players = list(self.tournament.get_remaining_players())

        # Créez des paires tout en évitant les répétitions
        for i in range(len(remaining_players)):
            player1 = remaining_players[i]

            for j in range(i + 1, len(remaining_players)):
                player2 = remaining_players[j]

                # Vérifiez si ces deux joueurs se sont déjà rencontrés
                if (player1, player2) not in pairs_history and (player2, player1) not in pairs_history:
                    new_match = Match(player1, player2)
                    controller_round.add_match_controller(new_match)

                    # Mettez à jour l'historique des paires
                    pairs_history.append((player1, player2))

                    break  # Sortez de la boucle interne

        # Mettez à jour le nombre de joueurs restants
        self.tournament.remove_players(remaining_players)


    controller_round.display_match_controller()

    print("Affichage Gagnant:")
    for match in controller_round.get_match_controller():
        controller_match = MatchController(match)
        controller_match.random_gagnant_controller()
        controller_match.save_match_to_json_controller()

    controller_tournoi.add_list_tournament_round_controller(round_tournament)

    score_instance = UpdateScoreRun(self.tournament, round_tournament)
    score_instance()

    controller_tournoi.score_player_tournament_controller()

    controller_tournoi.save_player_tournament_to_json_controller()
    controller_round.save_round_to_json_controller()
    controller_round.save_match_round_to_json_controller()
    controller_tournoi.save_round_tournament_to_json_controller()

    controller_round.set_termine_controller(datetime.now().isoformat())

print(f"***********************Fin tournoi***************\n")