# Professional Diagnostic Scanner Operation — Lessons 1.1 to 10.10

<!-- ONE file for all lessons 1.1 → 10.10. Append each new lesson at the END, in order. -->

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

---

### Module 1 — Professional Diagnostic Scanner Operation

### Lesson 1.2: Diagnostic Scanner Types and Functions

This lesson follows the five sections in your official handbook:

1.2.1 Basic code readers 1.2.2 Professional multibrand scanners 1.2.3 OEM diagnostic systems 1.2.4 Pass-through programming devices 1.2.5 EV and hybrid-specific equipment

The objective is to understand the capabilities and limitations of each diagnostic tool and select the correct equipment for a professional EV or hybrid workshop.

### 1.2.1 Basic code readers

A basic code reader is an entry-level diagnostic device designed primarily to retrieve and clear supported diagnostic trouble codes.

### Main functions

* Read supported generic OBD-II DTCs.

* Display basic fault descriptions.

* Clear supported DTCs.

* Display selected standardized live-data parameters.

* Retrieve supported freeze-frame information.

* Display emissions readiness monitor status.

### How it works

* Connect the code reader to the vehicle's diagnostic connector.

* Switch the ignition or vehicle to the required diagnostic power state.

* Select the diagnostic function.

* The reader sends a request through its communication interface.

* The ECU responds with available diagnostic information.

* The reader displays the result.

### Workshop example

A hybrid vehicle displays a malfunction indicator lamp.

A basic reader retrieves a generic powertrain DTC. This provides an initial diagnostic direction, but may not provide the detailed hybrid battery, inverter or motor-control information needed to identify the root cause.

Limitation: A basic reader should not be mistaken for a complete vehicle diagnostic system.

### 1.2.2 Professional multibrand scanners

A professional multibrand scanner is designed to communicate with multiple vehicle manufacturers and access more diagnostic functions than a basic code reader.

These scanners are widely used in independent automotive workshops.

### Main functions

1\. Full-system scanning

Can scan multiple supported ECUs, such as:

* Engine control module

* Transmission control module

* ABS/ESC

* Airbag system

* Body control module

* Hybrid control system

* Battery management system, where supported

2\. Advanced DTC functions

Can retrieve manufacturer-specific fault codes and additional ECU information when supported by the vehicle and scanner software.

3\. Live-data analysis

Displays operating parameters such as:

* Battery voltage

* Coolant temperature

* Motor speed

* Sensor signals

* ECU supply voltage

* Charging-system parameters

4\. Bidirectional control

Can command supported components to operate.

Examples include:

* Cooling fan activation.

* Coolant pump activation.

* Relay activation.

* Selected actuator tests.

5\. Service functions

Depending on vehicle coverage:

* Electronic parking brake service.

* Steering-angle calibration.

* Battery registration.

* Throttle adaptation.

* Component initialization.

### Professional advantage

A multibrand scanner provides broad vehicle coverage without requiring a separate manufacturer-specific tool for every vehicle.

### Important limitation

Not all multibrand scanners have equal coverage. Two scanners may support the same vehicle but provide different access to BMS data, active tests, coding and programming.

Always verify the exact vehicle model, production year, ECU and function coverage.

### 1.2.3 OEM diagnostic systems

An OEM diagnostic system is manufacturer-specific equipment or software designed to support diagnosis, maintenance and programming of that manufacturer's vehicles.

Examples include:

* Toyota Techstream

* BMW ISTA

* Mercedes-Benz XENTRY

* Volkswagen ODIS

* Ford FDRS

### Main capabilities

1\. Manufacturer-specific ECU access

Provides access to manufacturer-specific diagnostic information and functions that may not be available through generic equipment.

2\. Guided diagnostics

Some OEM systems provide structured diagnostic procedures that guide the technician through tests based on the vehicle's fault information.

3\. Advanced live data

May expose manufacturer-specific parameters that are important for EV and hybrid diagnosis.

For example:

* Individual battery block voltage.

* Battery temperature sensor readings.

* Contactor status.

* Inverter operating temperatures.

* Motor resolver information.

* Charging-system operating status.

4\. ECU programming and configuration

Where supported and authorized, OEM systems may perform:

* ECU software updates.

* Coding and configuration.

* Adaptations.

* Component initialization.

* Calibration procedures.

### Why OEM tools matter

Consider a hybrid vehicle with a battery-system warning.

A multibrand scanner may identify a battery-related DTC. An OEM system may provide a more detailed manufacturer-specific diagnostic procedure, relevant battery parameters and prescribed testing sequence.

However, OEM diagnostic access does not remove the need for independent verification of electrical and mechanical faults.

### 1.2.4 Pass-through programming devices

A pass-through programming device is an interface that allows compatible computer-based diagnostic or programming software to communicate with vehicle ECUs.

One important standard associated with this equipment is SAE J2534.

### Main purpose

It provides a communication pathway between:

* A computer running diagnostic or programming software.

* A vehicle communication interface.

* The vehicle's diagnostic connector.

* The target ECU.

### Simplified architecture

Laptop / PC

OEM programming application

J2534 pass-through interface

Communication hardware and driver

Vehicle DLC / communication network

Target ECU

Receives supported programming or diagnostic communication

Simplified programming architecture. Actual interfaces and supported protocols depend on the vehicle, software and device.

### Typical applications

* ECU reprogramming.

* Manufacturer-authorized software updates.

* Selected ECU diagnostic functions.

* Calibration or configuration procedures where supported.

### Critical programming precautions

Programming is not the same as ordinary DTC scanning.

Before programming:

* Confirm the correct vehicle and ECU.

* Verify the ECU part number and software compatibility.

* Confirm stable vehicle power.

* Use the manufacturer-specified battery support equipment and voltage requirements.

* Confirm the communication interface and software compatibility.

* Follow the OEM programming procedure.

* Verify programming completion and perform required post-programming checks.

Programming risk

Interrupted or incorrect ECU programming can leave a control module unable to operate correctly. Some modules may require recovery procedures or replacement. Never interrupt programming power or communication unless the manufacturer procedure explicitly instructs you to do so.

### 1.2.5 EV and hybrid-specific equipment

EV and hybrid vehicles require diagnostic equipment capable of accessing their specialized high-voltage and electrified powertrain systems.

### A. EV-capable diagnostic scanner

A suitable EV-capable scanner may access:

* Battery Management System.

* Battery cell or block voltage.

* Battery temperature readings.

* State of Charge (SoC).

* State of Health (SoH), where supported.

* Battery contactor status.

* Inverter control data.

* Electric motor operating parameters.

* Onboard charger information.

* DC-DC converter data.

* Charging-system DTCs.

Actual access depends on vehicle coverage and manufacturer restrictions.

### B. High-voltage insulation resistance tester

An insulation resistance tester is used to evaluate electrical insulation resistance under the manufacturer's specified testing conditions.

It is relevant when investigating suspected insulation deterioration in HV circuits.

Important distinctions:

* It is not an ordinary multimeter.

* It applies a specified test voltage.

* It must only be used on isolated circuits and components approved for that test.

* Electronic modules, capacitors and other sensitive components may be damaged by inappropriate test voltage.

Never apply an insulation tester to a connected HV system or ECU without an approved manufacturer procedure.

### C. High-voltage measurement equipment

Specialized HV-rated equipment is required for measurements on high-voltage circuits.

Examples include:

* Properly rated digital multimeters.

* Approved HV measurement leads and probes.

* Suitable current measurement equipment.

* Manufacturer-approved breakout adapters where required.

The equipment's voltage rating, measurement category, probe condition and operating procedure must be appropriate for the circuit being tested.

### D. Battery diagnostic equipment

Depending on the vehicle and battery design, specialized battery equipment may support:

* Battery pack evaluation.

* Module or cell assessment.

* Voltage measurement.

* Capacity testing.

* Internal resistance evaluation.

* Battery balancing or reconditioning procedures where permitted.

Not every battery analyzer supports every EV battery chemistry or architecture.

### 6\. Professional equipment selection

| Diagnostic task                 | Appropriate equipment                               |
| ------------------------------- | --------------------------------------------------- |
| Basic generic DTC retrieval     | Basic OBD-II reader                                 |
| Multi-system diagnosis          | Professional multibrand scanner                     |
| Manufacturer-specific diagnosis | OEM diagnostic system                               |
| Supported ECU programming       | OEM software with compatible pass-through interface |
| HV insulation testing           | Approved insulation resistance tester               |
| HV voltage measurement          | Properly rated HV measurement equipment             |
| Battery condition evaluation    | Compatible battery diagnostic equipment             |

### 7\. Workshop scenario

Vehicle: Battery-electric vehicle (BEV)

Customer complaint: Vehicle displays an electric powertrain warning and has reduced power.

A professional technician should select equipment based on the diagnostic objective:

* Use an EV-capable scanner with confirmed vehicle coverage.

* Identify the BMS, VCU and inverter ECUs.

* Retrieve and save all relevant DTCs.

* Examine relevant live data.

* Compare measured or reported values with manufacturer specifications.

* Use additional electrical test equipment only when the diagnostic evidence indicates a need.

* Confirm the root cause before replacing components.

Do not assume that a battery warning means the battery pack itself has failed. The fault could originate from sensing, wiring, power supply, communication, thermal management or another associated system.

### Lesson 1.2 — Technical conclusions

* Basic code readers are suitable for limited standardized diagnostic access.

* Professional multibrand scanners provide broader system coverage and service functions.

* OEM systems provide manufacturer-specific diagnostic capabilities.

* J2534 pass-through devices provide a communication interface for supported programming applications.

* EV and hybrid diagnosis requires specialized scanner coverage and appropriately rated electrical test equipment.

* Equipment selection must be based on the vehicle, ECU, diagnostic objective and manufacturer procedure.

Next lesson: Module 1, Lesson 1.3 — Vehicle Identification and Diagnostic Connection.

This will cover VIN identification and decoding, vehicle selection, DLC connector identification, communication protocols and secure gateway access.

Official lesson structure: uploaded handbook, Module 1, Section 1.2.

---

<!-- NEXT: Lesson 1.3 — Vehicle Identification and Diagnostic Connection (append below) -->
