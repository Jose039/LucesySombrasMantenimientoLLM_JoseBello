"""
Payroll Management CLI (Refactored)

This module provides a clean, type-annotated, and documented refactor of the
original imperative payroll script. It defines clear data structures, separates
logic from input/output, and centralizes repeated calculations.

Behavioral parity:
- Department-specific tax rates are preserved: Sales/IT at 15%, HR at 16%.
- Fixed cafeteria deduction of 50 is applied to all departments.
- Net pay never goes below 0.
- CLI options 1-5 are kept functionally equivalent to the original.

Run this file directly to launch the interactive CLI.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class Department(Enum):
    """Enumeration of supported departments and their tax rates."""

    SALES = "Ventas"
    IT = "IT"
    HR = "RRHH"

    @property
    def tax_rate(self) -> float:
        """Return the income tax rate for the department.

        Returns:
            float: The tax rate as a fraction (e.g., 0.15 for 15%).
        """
        if self is Department.HR:
            return 0.16
        # Sales and IT share same rate in the original implementation
        return 0.15


CAFETERIA_DEDUCTION: float = 50.0


@dataclass(frozen=True)
class Employee:
    """Represents an employee and their payroll-related data.

    Attributes:
        name: Employee full name.
        department: Department they belong to.
        gross_salary: Gross salary before deductions.
        net_salary: Calculated net salary after tax and cafeteria deduction.
    """

    name: str
    department: Department
    gross_salary: float
    net_salary: float


def calculate_net_salary(gross_salary: float, department: Department) -> float:
    """Compute the net salary for a given gross salary and department.

    Applies department-specific tax and the fixed cafeteria deduction. Net salary
    is floored at 0.

    Args:
        gross_salary: The gross salary value (must be non-negative).
        department: The department used to determine the tax rate.

    Returns:
        Net salary after deductions, never negative.

    Raises:
        ValueError: If gross_salary is negative.
    """
    if gross_salary < 0:
        raise ValueError("Gross salary cannot be negative.")

    tax = gross_salary * department.tax_rate
    net = gross_salary - tax - CAFETERIA_DEDUCTION
    return max(net, 0.0)


class PayrollSystem:
    """In-memory payroll registry with simple reporting capabilities."""

    def __init__(self) -> None:
        self._employees: List[Employee] = []

    def add_employee(self, name: str, department: Department, gross_salary: float) -> Employee:
        """Create and register a new employee.

        Args:
            name: Employee name.
            department: Department assignment.
            gross_salary: Gross salary amount.

        Returns:
            The newly created Employee instance with computed net salary.
        """
        net_salary = calculate_net_salary(gross_salary, department)
        employee = Employee(name=name, department=department, gross_salary=gross_salary, net_salary=net_salary)
        self._employees.append(employee)
        return employee

    def list_employees(self) -> List[Employee]:
        """Return all registered employees in insertion order."""
        return list(self._employees)

    def is_empty(self) -> bool:
        """Return True if no employees have been registered."""
        return not self._employees


# ------------- CLI helpers -------------

def _prompt_non_empty(prompt: str) -> str:
    """Prompt for a non-empty string.

    Args:
        prompt: The message to show to the user.

    Returns:
        The user's non-empty input string.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Entrada vacía. Intente nuevamente.")


def _prompt_float(prompt: str) -> float:
    """Prompt for a float input.

    Args:
        prompt: The message to show to the user.

    Returns:
        The parsed float value.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            return value
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")


def _print_header() -> None:
    """Prints the application header banner."""
    print("********************************")
    print("SISTEMA DE NOMINAS V2.3 FINAL_REAL_AHORA_SI (Refactor)")
    print("********************************")


def _print_menu() -> None:
    """Display the main menu options."""
    print("")
    print("1. Agregar empleado Ventas")
    print("2. Agregar empleado IT")
    print("3. Agregar empleado RRHH")
    print("4. Ver reporte")
    print("5. Salir")
    print("")


def _handle_add_employee(system: PayrollSystem, department: Department) -> None:
    """Interactively add an employee for a given department.

    Args:
        system: The payroll system to mutate.
        department: The department to assign to the new employee.
    """
    name = _prompt_non_empty("Nombre: ")
    gross = _prompt_float("Sueldo Bruto: ")
    try:
        employee = system.add_employee(name, department, gross)
        print(f"Guardado {employee.department.value}.")
    except ValueError as exc:
        print(f"Error: {exc}")


def _print_report(system: PayrollSystem) -> None:
    """Print a simple report of all employees and their net pay."""
    if system.is_empty():
        print("No hay nadie")
        return

    for employee in system.list_employees():
        print(f"Emp: {employee.name}")
        print(f"Depto: {employee.department.value}")
        print(f"Pago Final: {employee.net_salary}")
        print("----------------")


def run_cli() -> None:
    """Launch the interactive payroll CLI loop."""
    _print_header()
    system = PayrollSystem()

    while True:
        _print_menu()
        choice = input("Seleccione opcion: ").strip()

        if choice == "1":
            _handle_add_employee(system, Department.SALES)
        elif choice == "2":
            _handle_add_employee(system, Department.IT)
        elif choice == "3":
            _handle_add_employee(system, Department.HR)
        elif choice == "4":
            _print_report(system)
        elif choice == "5":
            break
        else:
            print("Error")


if __name__ == "__main__":
    run_cli()
