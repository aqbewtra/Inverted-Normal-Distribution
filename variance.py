from scipy.optimize import fsolve
import torch

torch.pi = torch.acos(torch.zeros(1)).item() * 2

def var(sigma):
    return torch.erf(torch.tensor(1/((2**(1/2))*sigma)))+ 1 - 2/(sigma*((2*torch.pi)**(1/2)))

if __name__ == "__main__":
    sigma = fsolve(var, .4)
    f = open("variance.txt", "w")
    f.write(str(sigma))
    f.close()