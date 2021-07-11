from torch import nn
import torch


class Network(nn.Module):
    def __init__(self, env, hidden_size=243):
        super().__init__()

        #in_features = int(np.prod(env.observation_space.shape))
        in_features = 27

        self.net = nn.Sequential(
            nn.Linear(in_features, hidden_size),
            nn.Tanh(),
            nn.Linear(hidden_size, env.action_space.n)
        )

    def forward(self, x):
        return self.net(x)

    def act(self, obs, env, device):
        obs_t = torch.as_tensor(obs, dtype=torch.float32, device=device)
        q_values = self(obs_t.unsqueeze(0))
        possible_values = env.list_of_valid_moves()

        for x in range(1, 10):
            if x not in possible_values:
                q_values[0][x - 1] = -10.0

        max_q_index = torch.argmax(q_values, dim=1)[0]
        action = max_q_index.detach().item()

        return action