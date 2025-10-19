class Controller:
    def __init__(self, KP: float = 0.15, KD : float = 0.7, KI: float = 0.01, dt: float = 1.0):
        self.KP = KP
        self.KD = KD
        self.KI = KI
        self.dt = dt
        self.previous_error = 0.0
        self.integral = 0.0

    def get_action(self, reference_depth: float, current_depth: float) -> float:
        error = reference_depth - current_depth
        derivative = ( error - self.previous_error ) / self.dt
        self.integral += error * self.dt
        action = self.KP * error + self.KD * derivative + self.KI * self.integral
        self.previous_error = error
        return action
    
    def reset(self):
        self.previous_error = 0.0
        self.integral = 0.0