### Feed Forward Layer
### GeLU Activation Function
import torch
import torch.nn as nn

class GELU(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x):
        return 0.5 * x * (1 + torch.tanh(
                            torch.sqrt(torch.tensor(2.0 / torch.pi)) * 
                                        (x + 0.044715 * torch.pow(x, 3))
                                        ))

class FeedForward(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(cfg["emb_dim"], cfg["emb_dim"] * 4),
            nn.GELU(),
            nn.Linear(cfg["emb_dim"] * 4, cfg["emb_dim"])
        )
    
    def forward(self, x):
        return self.layers(x)
