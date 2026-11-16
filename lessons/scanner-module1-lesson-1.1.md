### Module 1 — Professional Diagnostic Scanner Operation

### Lesson 1.1: Introduction to Professional Diagnostic Scanners

This lesson follows your uploaded handbook structure exactly:

1.1.1 Purpose of automotive diagnostic scanners 1.1.2 Diagnostic scanner architecture 1.1.3 Generic OBD-II scanners versus OEM tools 1.1.4 Scanner hardware and software components

The focus is professional workshop diagnosis, including electric and hybrid vehicles—not simply reading and clearing fault codes.

### 1.1.1 Purpose of automotive diagnostic scanners

A professional automotive diagnostic scanner is an electronic service tool that communicates with a vehicle’s Electronic Control Units (ECUs) to retrieve information, identify faults, monitor operating parameters and perform supported diagnostic or service functions.

Modern vehicles contain multiple electronic control modules. In an EV or hybrid, these may include:

* BMS — Battery Management System

* VCU — Vehicle Control Unit

* MCU / Inverter Control Unit — traction motor control

* OBC — Onboard Charger

* DC-DC Converter Control Unit

* ABS/ESC — braking and stability control

* EPS — Electric Power Steering

* HVAC Control Unit — heating, ventilation and air conditioning

* Gateway ECU — communication between vehicle networks

A scanner allows a technician to access information from these modules without dismantling the vehicle or directly probing every circuit.

### Main diagnostic purposes

1\. Fault-code retrieval

The scanner reads Diagnostic Trouble Codes (DTCs) stored by vehicle control modules.

Example:

* A BMS may report a battery voltage deviation fault.

* An inverter ECU may report a motor-position sensor fault.

* A DC-DC converter may report an output-voltage fault.

A DTC identifies a detected fault condition. It does not automatically prove which component has failed.

2\. Live-data monitoring

The scanner displays real-time or periodically updated values transmitted by an ECU.

Examples of EV live data include:

| Parameter            | What the technician evaluates         |
| -------------------- | ------------------------------------- |
| HV battery voltage   | Total pack voltage                    |
| Cell voltage         | Individual cell or cell-group voltage |
| Battery current      | Charge or discharge current           |
| Battery temperature  | Temperature sensor readings           |
| Isolation resistance | Reported HV insulation condition      |
| Motor speed          | Traction motor rotational speed       |
| Inverter temperature | Power-electronics thermal condition   |
| DC-DC output voltage | Low-voltage supply performance        |

3\. ECU identification

The scanner can identify responding control modules and, where supported, retrieve details such as ECU part number, software version and calibration identification.

4\. Active tests

Some scanners can command an ECU to operate a component, such as a cooling fan, coolant pump or relay. This is called bidirectional control.

5\. Service functions

Depending on vehicle and scanner capability, service functions may include calibration, initialization, adaptation and maintenance resets.

Important workshop principle: A scanner is a diagnostic information and control interface. It does not replace electrical measurements, wiring-diagram analysis, physical inspection or manufacturer diagnostic procedures.

### 1.1.2 Diagnostic scanner architecture

To diagnose a vehicle correctly, understand the communication path between the scanner and the vehicle ECU.

A typical diagnostic connection follows this sequence:

Diagnostic scanner

Displays data, sends requests and executes supported commands

Diagnostic cable or wireless interface

DLC — Data Link Connector

Physical diagnostic access point, commonly the 16-pin OBD connector

Vehicle communication network

Gateway ECU / Network interface

Routes or controls diagnostic communication where applicable

BMS

VCU

Inverter ECU

OBC / DC-DC

ABS / ESC

HVAC ECU

Simplified conceptual architecture. Actual network topology, gateway arrangement and diagnostic paths vary by manufacturer and vehicle platform.

### How communication works

* The technician selects the correct vehicle and diagnostic system.

* The scanner sends a diagnostic request.

* The vehicle network carries the request to the relevant ECU, directly or through a gateway.

* The ECU processes the request and returns a response if the service is supported and access is permitted.

* The scanner decodes the response and displays the information.

### Important communication concepts

* Diagnostic request: A message sent by the scanner to an ECU.

* Diagnostic response: Information returned by the ECU.

* Protocol: The rules governing message format and communication.

* Gateway: A module that routes or filters communication between network segments.

* DLC: The physical diagnostic connector used to access the vehicle network.

Not every ECU is necessarily accessible through the standard OBD-II connector. Some manufacturer-specific systems require additional access, a dedicated interface or security authorization.

### 1.1.3 Generic OBD-II scanners versus OEM tools

There are two important categories of diagnostic access: generic OBD-II tools and manufacturer-specific diagnostic systems.

### A. Generic OBD-II scanner

A generic OBD-II scanner primarily accesses standardized emissions-related diagnostic information in vehicles that support the applicable OBD-II requirements.

Common functions include:

* Reading supported generic powertrain DTCs.

* Clearing supported DTCs.

* Displaying supported standardized live data.

* Viewing supported freeze-frame information.

* Checking emissions readiness monitors.

Limitation: A basic generic scanner may not access manufacturer-specific EV battery, inverter, charging, hybrid-control or body-system information.

### B. OEM diagnostic tool

An OEM diagnostic tool is designed for a particular vehicle manufacturer or vehicle group.

It may provide access to:

* Manufacturer-specific DTC descriptions.

* Expanded ECU identification.

* Detailed BMS parameters.

* Inverter and motor-control data.

* Hybrid-system diagnostic routines.

* Guided diagnostic procedures.

* Bidirectional tests.

* ECU programming and configuration functions, where authorized.

### Comparison

| Capability                  | Generic OBD-II         | OEM diagnostic tool |
| --------------------------- | ---------------------- | ------------------- |
| Standardized emissions DTCs | Yes, if supported      | Yes, if supported   |
| Manufacturer-specific DTCs  | Limited or unavailable | Usually extensive   |
| Full vehicle scan           | Usually limited        | Platform-dependent  |
| EV battery data             | Usually limited        | Often available     |
| Hybrid-system diagnosis     | Limited                | Often extensive     |
| Active tests                | Limited                | Vehicle-dependent   |
| ECU programming             | Generally no           | May be supported    |

Workshop example

A vehicle arrives with a warning message indicating an electric powertrain fault.

A generic scanner may retrieve a standardized powertrain code, if one is reported through its supported diagnostic services. An OEM tool may additionally access the BMS, inverter and VCU, retrieve manufacturer-specific fault information and display relevant operating parameters.

The correct approach is to use the tool that provides the diagnostic coverage required by the vehicle—not to assume that every scanner can access every ECU.

### 1.1.4 Scanner hardware and software components

A professional diagnostic system has several components working together.

### A. Hardware components

| Component                             | Technical function                                                       |
| ------------------------------------- | ------------------------------------------------------------------------ |
| Display unit                          | Shows DTCs, live data, test results and diagnostic menus                 |
| Processor                             | Executes scanner software and processes diagnostic information           |
| Memory / storage                      | Stores software, vehicle databases and diagnostic reports                |
| VCI — Vehicle Communication Interface | Provides the communication link between the scanner and vehicle          |
| Diagnostic cable                      | Connects the VCI to the vehicle DLC or another specified diagnostic port |
| Wireless interface                    | Provides supported Bluetooth or Wi-Fi communication                      |
| Power supply / battery                | Powers the diagnostic equipment                                          |

VCI is particularly important. It acts as the communication interface between the diagnostic software and vehicle networks. A scanner may have advanced software but still fail to communicate properly if its VCI is incompatible, defective or incorrectly configured.

### B. Software components

Professional scanner software typically contains:

* Vehicle database: Manufacturer, model, year and powertrain information.

* Diagnostic protocols: Communication services and message-handling functions.

* ECU software support: Functions for communicating with supported control modules.

* DTC database: Fault-code descriptions and diagnostic information.

* Live-data software: Displays, records and graphs ECU parameters.

* Special-function software: Supports authorized service routines and calibrations.

* Programming software: Supports ECU programming on compatible systems and equipment.

### C. Software updates and compatibility

Scanner software must be maintained because manufacturers introduce new vehicle models, ECUs, communication protocols and diagnostic functions.

Before starting diagnosis, check:

* Scanner software version.

* VCI firmware version.

* Vehicle coverage.

* ECU communication compatibility.

* Required security authorization.

* Internet or manufacturer-server requirements, where applicable.

A communication failure does not automatically mean the ECU is defective. The cause could be an incorrect vehicle selection, incompatible software, VCI malfunction, power-supply problem, network fault or restricted diagnostic access.

### Professional workshop application

Example: EV arrives with a powertrain warning.

A technician should follow a structured initial process:

* Confirm the vehicle VIN, model, year and powertrain.

* Check the 12 V supply condition and relevant vehicle power state.

* Identify the correct diagnostic connector and approved interface.

* Connect the scanner using the manufacturer's procedure.

* Perform an initial vehicle scan.

* Record responding and non-responding ECUs.

* Retrieve DTCs and save the original diagnostic report.

* Identify which additional live data or tests are required.

Do not clear DTCs before recording the original fault information. Do not activate high-voltage components or perform programming simply to see whether a fault disappears.

High-voltage diagnostic safety

A diagnostic scanner does not isolate or de-energize an HV system. Reading data through a diagnostic connector does not authorize physical work on HV components.

Follow the vehicle manufacturer's HV isolation procedure, required PPE, lockout/tagout requirements and prove-test-prove verification before any work that requires the HV system to be de-energized. Never use a scanner as proof that an HV circuit is safe to touch.

### Lesson 1.1 — Key technical points

* A diagnostic scanner communicates with vehicle ECUs through supported diagnostic interfaces and networks.

* A DTC identifies a detected fault condition; it does not by itself establish root cause.

* Generic OBD-II access is not equivalent to full manufacturer-level diagnostic coverage.

* The VCI is a critical link between the scanner and the vehicle.

* Scanner hardware, software, vehicle coverage and communication compatibility must all be considered.

* Diagnostic scanning is one part of a complete evidence-based diagnostic process.

Next lesson: Module 1, Lesson 1.2 — Diagnostic Scanner Types and Functions, covering basic code readers, professional multibrand scanners, OEM systems, pass-through programming devices and EV/hybrid-specific equipment.

Source structure: Your uploaded EV & Hybrid Master Technician Handbook – Complete Table of Contents, Module 1, Lesson 1.1.
