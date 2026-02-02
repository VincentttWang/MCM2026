import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

class ODESolver:
    def __init__(self, model_func):
        """
        model_func: callable(t, y, *args) -> dy/dt
        """
        self.model_func = model_func
    
    def solve(self, y0, t_span, t_eval=None, args=()):
        """
        Solves the ODE system.
        y0: initial conditions
        t_span: (t_start, t_end)
        t_eval: time points to evaluate (optional)
        args: additional arguments for model_func
        """
        solution = solve_ivp(self.model_func, t_span, y0, t_eval=t_eval, args=args)
        return solution

# --- Common Models ---

def logistic_growth(t, P, r, K):
    """
    dP/dt = r * P * (1 - P/K)
    """
    return r * P * (1 - P/K)

def seir_model(t, y, beta, sigma, gamma):
    """
    S: Susceptible, E: Exposed, I: Infectious, R: Recovered
    dS/dt = -beta * S * I
    dE/dt = beta * S * I - sigma * E
    dI/dt = sigma * E - gamma * I
    dR/dt = gamma * I
    """
    S, E, I, R = y
    dSdt = -beta * S * I
    dEdt = beta * S * I - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]

def lotka_volterra(t, y, alpha, beta, delta, gamma):
    """
    Predator-Prey Model
    x: Rabbit (Prey), y: Fox (Predator)
    dx/dt = alpha*x - beta*x*y
    dy/dt = delta*x*y - gamma*y
    """
    x, predator = y
    dxdt = alpha * x - beta * x * predator
    dydt = delta * x * predator - gamma * predator
    return [dxdt, dydt]

if __name__ == "__main__":
    # 1. Logistic Growth Test
    print("--- Logistic Growth Test ---")
    r, K = 0.5, 100
    solver = ODESolver(logistic_growth)
    t_eval = np.linspace(0, 20, 100)
    sol = solver.solve([10], (0, 20), t_eval=t_eval, args=(r, K))
    
    # Plotting is commented out to avoid blocking execution, but ready to use
    # plt.plot(sol.t, sol.y[0], label='Population')
    # plt.xlabel('Time')
    # plt.ylabel('Population')
    # plt.title('Logistic Growth')
    # plt.show()
    print("Logistic Sol shape:", sol.y.shape)

    # 2. SEIR Model Test
    print("\n--- SEIR Model Test ---")
    # Parameters
    N = 1000
    beta = 1.5 / N  # Infection rate
    sigma = 0.1     # Incubation rate
    gamma = 0.2     # Recovery rate
    
    # Initial conditions: S=990, E=10, I=0, R=0
    y0 = [990, 10, 0, 0]
    
    solver = ODESolver(seir_model)
    sol_seir = solver.solve(y0, (0, 100), t_eval=np.linspace(0, 100, 200), args=(beta, sigma, gamma))
    print("SEIR Final State:", sol_seir.y[:, -1])
    
    # 3. Lotka-Volterra Test
    print("\n--- Predator-Prey Test ---")
    solver = ODESolver(lotka_volterra)
    sol_lv = solver.solve([10, 5], (0, 50), t_eval=np.linspace(0, 50, 200), args=(1.1, 0.4, 0.1, 0.4))
    print("Predator-Prey Sol shape:", sol_lv.y.shape)
