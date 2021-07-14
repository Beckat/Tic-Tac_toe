import GameEngine as TicTacToe
import Neural_Network as Neural_Network
import torch

if torch.cuda.is_available():
    device = torch.device("cuda:0")  # you can continue going on here, like cuda:1 cuda:2....etc.
    print("Running on the GPU")
else:
    device = torch.device("cpu")
    print("Running on the CPU")

env = TicTacToe.GameEngine()

test_1_hidden_size = Neural_Network.Network(env, 1)
test_125_hidden_size = Neural_Network.Network(env, 125)
test_50_hidden_size = Neural_Network.Network(env, 50)
test_1_hidden_size.load_state_dict(torch.load("/home/danthom1704/PycharmProjects/Tic-Tac_toe/nn_tic_tac_toe_target_1"))
test_125_hidden_size.load_state_dict(torch.load("/home/danthom1704/PycharmProjects/Tic-Tac_toe/nn_tic_tac_toe_target_125"))
test_50_hidden_size.load_state_dict(torch.load("/home/danthom1704/PycharmProjects/Tic-Tac_toe/nn_tic_tac_toe_target_50"))
test_1_hidden_size.to(device)
test_125_hidden_size.to(device)
test_50_hidden_size.to(device)

obs = env.reset()

test_1_hidden_size_wins_going_first = 0
test_125_hidden_size_wins_going_second = 0
test_50_hidden_size_wins_going_second = 0
ties_1_going_first = 0
test_1_hidden_size_wins_going_second = 0
test_125_hidden_size_wins_going_first = 0
test_50_hidden_size_wins_going_first = 0
ties_125_going_first = 0
ties_50_going_first = 0

for x in range(1, 10):
    obs = env.reset()
    env.update_square("X", x)
    while not env.is_winner("X") and not env.is_winner("O"):
        env.game_board.print_grid()
        print("")

        obs = env.get_ai_state('O')
        env.update_square('O', test_125_hidden_size.act(obs, env, device) + 1)
        env.game_board.print_grid()
        print("")
        if env.is_winner("O"):
            test_125_hidden_size_wins_going_second = test_125_hidden_size_wins_going_second + 1
            break

        obs = env.get_ai_state('X')
        env.update_square('X', test_1_hidden_size.act(obs, env, device) + 1)
        env.game_board.print_grid()
        print("")

        if env.is_winner("X"):
            test_1_hidden_size_wins_going_first = test_1_hidden_size_wins_going_first + 1
            break

        if len(env.list_of_valid_moves()) == 0:
            ties_1_going_first = ties_1_going_first + 1
            break

print("")
print("")
for x in range(1, 10):
    obs = env.reset()
    env.update_square("X", x)
    while not env.is_winner("X") and not env.is_winner("O"):
        env.game_board.print_grid()
        print("")

        obs = env.get_ai_state('O')
        env.update_square('O', test_1_hidden_size.act(obs, env, device) + 1)
        env.game_board.print_grid()
        print("")
        if env.is_winner("O"):
            test_1_hidden_size_wins_going_second = test_1_hidden_size_wins_going_second + 1
            break

        obs = env.get_ai_state('X')
        env.update_square('X', test_125_hidden_size.act(obs, env, device) + 1)
        env.game_board.print_grid()
        print("")

        if env.is_winner("X"):
            test_125_hidden_size_wins_going_first = test_125_hidden_size_wins_going_first + 1
            break

        if len(env.list_of_valid_moves()) == 0:
            ties_125_going_first = ties_125_going_first + 1
            break


print("1 Wins Going First vs 125: ", test_1_hidden_size_wins_going_first)
print("125 Wins Going Second: ", test_125_hidden_size_wins_going_second)
print("Ties 1 Going First vs 125: ", ties_1_going_first)


print("1 Wins Going Second: ", test_1_hidden_size_wins_going_second)
print("125 Wins Goind First: ", test_125_hidden_size_wins_going_first)
print("Ties 125 Going First: ", ties_125_going_first)

ties_1_going_first_round_2 = 0
test_1_hidden_size_wins_going_first_round_2 = 0
test_1_hidden_size_wins_going_second_round_2 = 0

for x in range(1, 10):
    obs = env.reset()
    env.update_square("X", x)
    while not env.is_winner("X") and not env.is_winner("O"):
        env.game_board.print_grid()
        print("")

        obs = env.get_ai_state('O')
        env.update_square('O', test_50_hidden_size.act(obs, env, device) + 1)
        env.game_board.print_grid()
        print("")
        if env.is_winner("O"):
            test_50_hidden_size_wins_going_second = test_50_hidden_size_wins_going_second + 1
            break

        obs = env.get_ai_state('X')
        env.update_square('X', test_1_hidden_size.act(obs, env, device) + 1)
        env.game_board.print_grid()
        print("")

        if env.is_winner("X"):
            test_1_hidden_size_wins_going_first_round_2 = test_1_hidden_size_wins_going_first_round_2 + 1
            break

        if len(env.list_of_valid_moves()) == 0:
            ties_1_going_first_round_2 = ties_1_going_first_round_2 + 1
            break

print("")
print("")
for x in range(1, 10):
    obs = env.reset()
    env.update_square("X", x)
    while not env.is_winner("X") and not env.is_winner("O"):
        env.game_board.print_grid()
        print("")

        obs = env.get_ai_state('O')
        env.update_square('O', test_1_hidden_size.act(obs, env, device) + 1)
        env.game_board.print_grid()
        print("")
        if env.is_winner("O"):
            test_1_hidden_size_wins_going_second_round_2 = test_1_hidden_size_wins_going_second_round_2 + 1
            break

        obs = env.get_ai_state('X')
        env.update_square('X', test_50_hidden_size.act(obs, env, device) + 1)
        env.game_board.print_grid()
        print("")

        if env.is_winner("X"):
            test_50_hidden_size_wins_going_first = test_50_hidden_size_wins_going_first + 1
            break

        if len(env.list_of_valid_moves()) == 0:
            ties_50_going_first = ties_50_going_first + 1
            break

print("1 Wins Going First vs 125: ", test_1_hidden_size_wins_going_first)
print("125 Wins Going Second: ", test_125_hidden_size_wins_going_second)
print("Ties 1 Going First vs 125: ", ties_1_going_first)


print("1 Wins Going Second vs 125: ", test_1_hidden_size_wins_going_second)
print("125 Wins Goind First: ", test_125_hidden_size_wins_going_first)
print("Ties 125 Going First: ", ties_125_going_first)

print("")

print("1 Wins Going First vs 50: ", test_1_hidden_size_wins_going_first_round_2)
print("50 Wins Going Second: ", test_50_hidden_size_wins_going_second)
print("Ties 50 Going First: ", ties_1_going_first_round_2)


print("1 Wins Going Second: vs 50: ", test_1_hidden_size_wins_going_second_round_2)
print("50 Wins Going First: ", test_50_hidden_size_wins_going_first)
print("Ties 50 Going First: ", ties_50_going_first)
