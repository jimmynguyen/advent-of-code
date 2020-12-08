# https://adventofcode.com/2015/day/7
import util


class Operation:
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    LSHIFT = "LSHIFT"
    RSHIFT = "RSHIFT"

    @staticmethod
    def values():
        return [Operation.AND,Operation.OR,Operation.NOT,Operation.LSHIFT,Operation.RSHIFT]

    @staticmethod
    def get_operation(wire):
        for operation in Operation.values():
            if operation in wire:
                return operation
        return None

    @staticmethod
    def is_operation(wire):
        return Operation.get_operation(wire) is not None

    @staticmethod
    def perform_operation(operation,a,b):
        if Operation.AND == operation:
            return a & b
        elif Operation.OR == operation:
            return a | b
        elif Operation.NOT == operation:
            return 65535 - b
        elif Operation.LSHIFT == operation:
            return a << b
        elif Operation.RSHIFT == operation:
            return a >> b


def get_value(v,signals):
    return signals[v] if v in signals.keys() else None if len(v) == 0 else int(v)


def create_signals_map(circuit):
    signals = dict()
    _circuit = []
    for wire in circuit:
        if not Operation.is_operation(wire):
            signal,target = tuple(x.strip() for x in wire.split("->"))
            if signal.isnumeric():
                signals[target] = get_value(signal,signals)
                continue
        _circuit.append(wire)
    circuit = _circuit
    while len(circuit) > 0:
        _circuit = []
        for wire in circuit:
            signal,target = tuple(x.strip() for x in wire.split("->"))
            operation = Operation.get_operation(wire)
            if operation is not None:
                a,b = tuple(x.strip() for x in signal.split(operation))
                if (a in signals.keys() or a.isnumeric() or a == "") and (b in signals.keys() or b.isnumeric()):
                    a = get_value(a,signals)
                    b = get_value(b,signals)
                    signals[target] = Operation.perform_operation(operation,a,b)
                    continue
            elif signal in signals.keys():
                signals[target] = signals[signal]
                continue
            _circuit.append(wire)
        circuit = _circuit
    return signals


def create_signals_map_2(circuit):
    signals = create_signals_map(circuit)
    _circuit = []
    for wire in circuit:
        if wire.endswith("-> b"):
            _circuit.append("{} -> b".format(signals["a"]))
        else:
            _circuit.append(wire)
    signals = create_signals_map(_circuit)
    return signals


def solve(circuit,create_signals_map):
    signals = create_signals_map(circuit)
    return signals["a"]


if __name__ == "__main__":
    day = 7
    inputs = [
        create_signals_map,
        create_signals_map_2
    ]
    test_outputs = [72]
    util.solve(day,inputs,test_outputs,solve)