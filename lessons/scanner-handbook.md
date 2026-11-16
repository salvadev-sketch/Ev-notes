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

This will cover VIN identification and decoding, vehicle selection, DLC connector identification, communication protocols and secure gateway access.

---

### Module 1 — Professional Diagnostic Scanner Operation

### Lesson 1.3: Vehicle Identification and Diagnostic Connection

This lesson follows your handbook's five sections:

1.3.1 VIN identification and decoding 1.3.2 Vehicle model, year and powertrain selection 1.3.3 DLC connector identification 1.3.4 Communication protocols 1.3.5 Secure gateway access

Workshop objective: Correctly identify the vehicle, select the appropriate diagnostic software and establish reliable communication with the intended control modules.

A diagnostic connection should never begin with randomly selecting a vehicle or connecting an incompatible interface. Incorrect vehicle identification can lead to incorrect ECU selection, misleading fault descriptions and inappropriate service procedures.

### 1.3.1 VIN identification and decoding

### What is a VIN?

The Vehicle Identification Number (VIN) is a standardized vehicle identification code used to distinguish an individual vehicle.

For most modern road vehicles, the VIN contains 17 characters.

It provides identification information that can include:

* Manufacturer.

* Vehicle attributes.

* Model or vehicle family.

* Model-year identifier.

* Assembly plant.

* Production sequence number.

### VIN structure

The VIN is commonly divided into three sections.

| Section | Character positions | Meaning                       |
| ------- | ------------------- | ----------------------------- |
| WMI     | 1–3                 | World Manufacturer Identifier |
| VDS     | 4–9                 | Vehicle Descriptor Section    |
| VIS     | 10–17               | Vehicle Identifier Section    |

Illustrative VIN structure

1–3

### WMI

Manufacturer

4–9

### VDS

Vehicle description

10–17

### VIS

Vehicle identity

The diagram shows the standard 17-character VIN division, not the exact meaning of every manufacturer's individual character.

### Where to locate the VIN

Common locations include:

* Lower dashboard, visible through the windscreen.

* Driver-side door aperture or door pillar.

* Manufacturer identification plate.

* Vehicle registration documents.

* Manufacturer-specific electronic vehicle information.

Always compare the physical vehicle identification with the documentation and scanner-reported identification where available.

### Model-year identification

The 10th VIN character commonly identifies the model year in VIN systems using the standard model-year coding convention.

However, do not confuse:

* Model year.

* Calendar year of manufacture.

* First registration year.

They can be different.

Technician's rule: Use the manufacturer's vehicle identification information when a VIN decoder does not provide enough detail for selecting the correct diagnostic system.

### 1.3.2 Vehicle model, year and powertrain selection

After identifying the VIN, the technician must select the correct vehicle in the diagnostic scanner.

### Information required

The scanner may request:

* Vehicle manufacturer.

* Model and model variant.

* Model year.

* Market or region.

* Engine or motor configuration.

* Transmission type.

* Powertrain type.

* ECU or system to be diagnosed.

### Why powertrain selection matters

A manufacturer may produce several versions of the same vehicle model:

| Vehicle version        | Diagnostic architecture                                     |
| ---------------------- | ----------------------------------------------------------- |
| Conventional petrol    | Engine ECU and conventional drivetrain modules              |
| Conventional diesel    | Diesel engine management and emissions systems              |
| Mild hybrid (MHEV)     | Engine ECU plus 48 V or other hybrid-related systems        |
| Full hybrid (HEV)      | Engine, motor-generator and hybrid control systems          |
| Plug-in hybrid (PHEV)  | Hybrid system plus externally rechargeable traction battery |
| Battery electric (BEV) | HV battery, inverter, motor and EV charging systems         |

Selecting the wrong version can result in:

* Incorrect ECU list.

* Missing diagnostic functions.

* Incorrect wiring information.

* Unsupported active tests.

* Incorrect service procedures.

### Professional selection procedure

* Read and record the VIN.

* Confirm the manufacturer and model.

* Confirm the model year and market.

* Identify the actual powertrain configuration.

* Select the matching vehicle in the scanner.

* Where supported, perform automatic VIN identification.

* Cross-check the scanner's identification against the physical vehicle.

Important: Automatic VIN recognition is useful, but it must be verified. Do not assume that automatic identification has correctly selected every vehicle variant.

### 1.3.3 DLC connector identification

### What is a DLC?

DLC means Data Link Connector.

It is the physical connection point through which compatible diagnostic equipment communicates with vehicle electronic systems.

Many modern vehicles use the standardized 16-pin OBD-II connector, also called the SAE J1962 connector.

### Common OBD-II connector pin functions

| Pin | Common function         |
| --- | ----------------------- |
| 4   | Chassis ground          |
| 5   | Signal ground           |
| 6   | CAN High                |
| 14  | CAN Low                 |
| 16  | Battery positive supply |

Other pins may be used for manufacturer-specific functions or other supported communication systems.

Not every pin is populated on every vehicle.

### Diagnostic connection procedure

* Locate the DLC using manufacturer service information.

* Inspect the connector for damaged pins, corrosion, contamination or loose terminals.

* Confirm the scanner cable and VCI are compatible.

* Connect the interface without forcing the connector.

* Establish the required vehicle ignition or power state.

* Select the correct vehicle and initiate communication.

* Confirm that the intended ECU responds.

### DLC power-supply considerations

The common pin 16 supply is normally provided by the vehicle's low-voltage electrical system.

If the scanner does not power up or cannot establish communication, investigate:

* Pin 16 supply.

* Pins 4 and 5 ground integrity.

* DLC fuse and supply circuit.

* Connector terminal condition.

* VCI and cable condition.

Do not assume that a communication failure means the ECU is defective.

Professional caution: Do not probe DLC terminals with oversized test probes or bridge pins. Use suitable breakout equipment and the correct wiring information.

### 1.3.4 Communication protocols

A communication protocol defines the rules that allow diagnostic equipment and vehicle ECUs to exchange data.

Different vehicles and electronic architectures may use different protocols.

### Common automotive diagnostic protocols

| Protocol                          | Main application                               |
| --------------------------------- | ---------------------------------------------- |
| ISO 9141-2                        | Older OBD communication                        |
| SAE J1850                         | Older OBD communication on supported vehicles  |
| ISO 14230 (KWP2000)               | Keyword Protocol 2000 diagnostic communication |
| ISO 15765 (CAN-based diagnostics) | Diagnostics over CAN                           |
| ISO 11898                         | CAN network technology                         |
| ISO 13400 (DoIP)                  | Diagnostics over Internet Protocol             |
| CAN FD                            | Higher-data-rate CAN communication             |

These standards are related but are not interchangeable. For example, ISO 11898 defines CAN communication technology, while ISO 15765 specifies diagnostic communication over CAN.

### A. CAN — Controller Area Network

CAN is widely used for communication between automotive electronic control units.

Important characteristics:

* Differential signalling using CAN High and CAN Low.

* Message-based communication.

* Multiple ECUs can share a network.

* Message priority is handled through arbitration.

* Diagnostic requests and responses can be transmitted over the network.

### B. CAN FD — CAN with Flexible Data Rate

CAN FD extends conventional CAN capabilities.

It supports:

* Larger data payloads per frame.

* Higher data rates during the data phase.

* More efficient transfer of larger diagnostic information.

A CAN FD-compatible vehicle interface is required when the diagnostic operation depends on CAN FD communication.

### C. DoIP — Diagnostics over Internet Protocol

DoIP enables automotive diagnostic communication over IP-based vehicle networks, commonly using Ethernet physical connections.

It can support high-bandwidth diagnostic communication, including programming operations on compatible vehicles.

### How the scanner identifies the protocol

Depending on the vehicle and scanner, protocol selection may be:

* Automatic.

* Determined by the selected vehicle profile.

* Configured through the diagnostic software.

* Specified by the manufacturer.

The technician should not manually select a protocol without confirming that it matches the vehicle's diagnostic architecture.

### 1.3.5 Secure gateway access

### What is a Secure Gateway?

A Secure Gateway (SGW) is a vehicle security mechanism that controls access to selected diagnostic functions and communication pathways.

It helps prevent unauthorized diagnostic commands from being sent to vehicle control modules.

Some manufacturers restrict certain diagnostic operations unless the technician or diagnostic tool has been authenticated.

### Why manufacturers use secure gateways

A vehicle diagnostic connector can provide access to important electronic systems. Without appropriate access controls, unauthorized users could potentially:

* Clear certain fault codes.

* Change ECU configurations.

* Activate selected actuators.

* Perform restricted service functions.

* Attempt unauthorized programming.

A secure gateway helps protect these systems.

### Diagnostic functions that may be restricted

Depending on the manufacturer and vehicle:

* DTC clearing.

* Active tests.

* Service resets.

* ECU coding.

* Adaptations.

* Programming and configuration.

Read-only functions may remain available, but this varies by platform.

### Secure gateway authorization process

A typical authorized workflow is:

* Connect a compatible diagnostic scanner.

* Identify the vehicle correctly.

* Establish communication with the gateway.

* Select the required restricted diagnostic function.

* Authenticate using the manufacturer's approved authorization method.

* Obtain permission for the requested operation.

* Perform the permitted diagnostic procedure.

* Verify the result and retain diagnostic records.

Authentication methods may include an approved online account, manufacturer subscription, security certificate or authorized diagnostic service.

### Important distinction

A secure gateway is not the same as a communication fault.

For example:

* Communication fault: The scanner cannot communicate because of a wiring, power, network or interface problem.

* Security restriction: The ECU or gateway is communicating, but the requested operation is not authorized.

A technician must distinguish these conditions before replacing modules or investigating wiring.

### Professional workshop procedure — Complete diagnostic connection

Consider a BEV arriving with a powertrain warning.

### Vehicle identification and connection workflow

* Identify the vehicle

    Record VIN, manufacturer, model, model year and powertrain.

* Select the vehicle profile

    Confirm the correct BEV variant and market in the scanner.

* Inspect the DLC

    Check connector condition, power supply and grounds using the correct procedure.

* Connect the VCI

    Use a compatible communication interface and cable.

* Establish communication

    Confirm the communication protocol and vehicle network access.

* Authenticate if required

    Use authorized secure gateway access for restricted functions.

* Confirm ECU communication

    Verify that the intended modules are responding before starting diagnosis.

### Common connection problems and diagnostic direction

| Symptom                                      | Possible cause to investigate                                       |
| -------------------------------------------- | ------------------------------------------------------------------- |
| Scanner does not power up                    | DLC supply, fuse, ground, cable or scanner fault                    |
| Vehicle identification incorrect             | Wrong VIN or vehicle profile                                        |
| No communication with any ECU                | Power supply, ground, network, VCI or gateway issue                 |
| Some ECUs respond, others do not             | ECU power, local network, gateway routing or module fault           |
| Read-only access works, active tests blocked | Secure gateway authorization or function restriction                |
| Communication drops intermittently           | Connector condition, voltage stability, wiring or network integrity |

These are diagnostic possibilities, not confirmed root causes. Always verify using the manufacturer's wiring diagrams and procedures.

### Lesson 1.3 — Key technical points

* The VIN is the starting point for correct vehicle identification.

* Model year, market and powertrain configuration must be verified.

* The DLC provides the physical diagnostic connection.

* CAN, CAN FD and DoIP are important communication technologies in modern vehicles.

* A communication failure must be distinguished from a secure gateway restriction.

* Correct vehicle identification and compatible diagnostic equipment are essential before performing tests or programming.

---

### Module 1 — Professional Diagnostic Scanner Operation

### Lesson 1.4: Complete Vehicle Health Scanning

A complete vehicle health scan is a systematic electronic inspection of the vehicle's control modules (ECUs). Its purpose is to establish the vehicle's overall electronic condition, identify faults across different systems, and create a reliable diagnostic baseline before repairs begin.

A professional technician does not simply connect a scanner, read a few codes, and start replacing components. The technician first establishes which modules are installed, which modules communicate, which faults are present, and how the faults relate to one another.

### 1.4.1 Initial Vehicle Health Check

Before connecting the diagnostic scanner, perform an initial inspection.

The objective is to understand the vehicle's condition and prevent misleading diagnostic results.

A. Confirm vehicle identity

Record:

* Vehicle identification number (VIN).

* Manufacturer, model and model year.

* Powertrain type: BEV, HEV, PHEV or conventional ICE.

* Odometer reading.

* Customer-reported symptoms.

* Warning indicators displayed on the instrument cluster.

B. Inspect vehicle electrical condition

Check:

* 12 V auxiliary battery condition.

* Battery terminals and connections.

* Relevant fuses and power supply circuits.

* Visible damage to wiring and connectors.

* Signs of water ingress or corrosion.

* Instrument cluster warning messages.

For EVs and hybrids, pay particular attention to the 12 V system. The low-voltage battery supplies power to many control modules and helps operate the high-voltage system's control circuits.

A weak 12 V supply can cause:

* Multiple ECU communication faults.

* Unexpected module resets.

* Contactor control problems.

* Unusual warning messages.

* Intermittent diagnostic communication.

Important: Do not assume that multiple communication DTCs mean multiple defective ECUs. First investigate common power supply, ground and network conditions.

C. Establish vehicle operating condition

Record whether the vehicle is:

* OFF.

* Ignition ON.

* READY.

* Charging.

* In a fault-related shutdown state.

The operating condition matters because some ECUs only communicate or become fully active under particular conditions.

### 1.4.2 ECU Identification

An Electronic Control Unit (ECU) is an electronic controller responsible for monitoring or controlling a particular vehicle function.

Modern EVs may contain many ECUs connected through different vehicle networks.

Examples include:

| ECU / Control module       | Main responsibility                    |
| -------------------------- | -------------------------------------- |
| BMS                        | Battery monitoring and protection      |
| VCU                        | Vehicle-level powertrain coordination  |
| MCU / Inverter controller  | Electric motor torque control          |
| OBC                        | AC charging control                    |
| DC-DC converter controller | High-voltage to low-voltage conversion |
| ABS / ESC                  | Braking and vehicle stability          |
| BCM                        | Body electrical functions              |
| TCM                        | Transmission control, where fitted     |
| HVAC controller            | Cabin heating and cooling              |
| EPS                        | Electric power steering                |
| SRS / Airbag ECU           | Occupant restraint systems             |

### What ECU identification tells the technician

A professional scanner may display:

* ECU name or system designation.

* Manufacturer identification.

* Hardware part number.

* Software identification or calibration ID.

* ECU communication status.

* VIN information, where supported.

* Diagnostic protocol information.

Example — Illustrative scanner data

| Parameter       | Example                   |
| --------------- | ------------------------- |
| Module          | Battery Management System |
| Hardware number | BMS-HW-204                |
| Software ID     | BMS_3.2.1                 |
| Communication   | Available                 |
| ECU voltage     | 13.8 V                    |
| DTC count       | 2                         |

These values are simulated for training, not readings from a real vehicle.

### Why software identification matters

Two vehicles of the same model and year may have different ECU software versions.

A technician should record software identification before programming or replacing a controller. Incorrect software or calibration can produce compatibility problems, unexpected operation or new DTCs.

### 1.4.3 Full-System Scanning

A full-system scan interrogates all accessible vehicle control modules rather than scanning only the engine or powertrain controller.

For an EV, the scan may include:

* Battery management system.

* Vehicle control unit.

* Inverter and motor controllers.

* Charging controllers.

* DC-DC converter.

* ABS and stability control.

* Electric power steering.

* HVAC.

* Body control.

* Restraint systems.

* Gateway and network controllers.

### Professional full-system scanning procedure

Step 1 — Connect the diagnostic interface

Connect the compatible diagnostic interface to the vehicle's DLC or approved diagnostic connection.

Step 2 — Identify the vehicle

Use VIN identification where supported. Confirm the selected model, year and powertrain manually.

Step 3 — Establish communication

Allow the scanner to identify the available vehicle networks and ECUs.

Step 4 — Select full-system scan

Choose the scanner's complete vehicle health check or equivalent function.

Step 5 — Allow interrogation to finish

Do not disconnect the interface or interrupt the scan while modules are being interrogated.

Step 6 — Save the scan results

Save the original report before clearing DTCs, performing resets or changing ECU settings.

### Example: Simulated EV full-system scan

| Module    | Communication | DTC count |
| --------- | ------------- | --------- |
| BMS       | Available     | 2         |
| VCU       | Available     | 1         |
| Inverter  | Available     | 0         |
| OBC       | Available     | 0         |
| DC-DC     | Available     | 0         |
| ABS / ESC | Available     | 1         |
| BCM       | Available     | 0         |
| HVAC      | No response   | —         |

This example shows why scanning the entire vehicle is important. A fault may exist outside the system initially suspected by the customer.

### 1.4.4 Communication Status and Unavailable Modules

One of the most important parts of a full-system scan is understanding module communication status.

A scanner may report:

* Available / Communicating: The ECU responded to the diagnostic request.

* No communication / No response: The scanner did not receive the expected response.

* Not installed / Not equipped: The vehicle configuration does not include that module.

* Communication error: Communication was attempted but an error occurred.

* Access denied: The diagnostic function may be restricted by security authorization.

These conditions are not interchangeable.

### How to diagnose an unavailable ECU

Imagine that the HVAC controller does not respond.

Do not immediately conclude that the HVAC ECU is defective.

Use a structured investigation:

1\. Confirm equipment configuration

Check whether the vehicle actually has the module.

2\. Check ECU power supply

Use the correct wiring diagram to identify the module's power supply circuits.

3\. Check ground circuits

Perform appropriate voltage-drop testing under the specified operating conditions.

4\. Check network communication

Identify whether the module communicates over CAN, CAN FD, LIN, Ethernet or another supported network.

5\. Inspect the network wiring

Look for damaged wiring, poor terminals, corrosion and connector problems.

6\. Consider gateway and security restrictions

Determine whether the module is inaccessible because of network routing, diagnostic authorization or secure gateway restrictions.

7\. Confirm the fault

Use manufacturer diagnostic procedures before deciding whether the ECU itself has failed.

### Important diagnostic distinction

A module that does not respond to a scanner is not automatically a failed module.

Possible causes include:

* Missing battery supply.

* Missing ignition or wake-up supply.

* Poor ground.

* Open or shorted communication wiring.

* Network termination or topology problems.

* Gateway restrictions.

* Incorrect vehicle selection.

* Faulty diagnostic interface.

* Defective ECU.

Workshop principle: Diagnose the power, ground and communication path before condemning the controller.

### 1.4.5 Diagnostic Report Generation

A diagnostic report is the recorded evidence of the vehicle's electronic condition at the time of inspection.

It is important for:

* Establishing a diagnostic baseline.

* Supporting repair decisions.

* Comparing before-and-after scan results.

* Communicating findings to other technicians.

* Documenting intermittent faults.

* Maintaining workshop service records.

### Information a professional report should contain

| Report section         | Required information                |
| ---------------------- | ----------------------------------- |
| Vehicle identification | VIN, model, year, powertrain        |
| Inspection details     | Date, mileage, operating condition  |
| Diagnostic equipment   | Scanner and software version        |
| ECU inventory          | Identified and accessible modules   |
| Communication status   | Available, unavailable, restricted  |
| Fault information      | DTCs and their status               |
| Supporting evidence    | Freeze-frame and relevant live data |
| Technician findings    | Confirmed observations              |
| Recommended action     | Further testing or repair           |
| Verification           | Post-repair scan and test results   |

### Before and after repair comparison

Consider this simulated example:

| Item               | Before repair | After repair |
| ------------------ | ------------- | ------------ |
| BMS communication  | Available     | Available    |
| BMS DTC count      | 2             | 0            |
| VCU communication  | Available     | Available    |
| HVAC communication | No response   | Available    |
| Full-system scan   | Incomplete    | Complete     |

The second scan suggests improvement, but a zero-DTC report alone does not prove that the vehicle is fully repaired. The technician must also confirm correct operation under the relevant operating conditions.

### Professional workshop workflow

### Complete Vehicle Health Scan

* Initial inspection

    Verify vehicle identity, 12 V condition and operating state.

* ECU identification

    Identify installed modules and record their software information.

* Full-system interrogation

    Scan all accessible ECUs and collect DTC information.

* Communication analysis

    Investigate unavailable modules and network-related faults.

* Report generation

    Save the original scan and document diagnostic evidence.

* Repair verification

    Repeat the scan and verify the affected systems operate correctly.

### Important safety considerations for EV and hybrid technicians

* A diagnostic scan does not require opening the high-voltage battery enclosure.

* Never disconnect HV components simply to improve scanner communication.

* Follow the manufacturer's vehicle operating-state requirements before running active tests.

* Do not perform insulation-resistance testing through connected ECUs or sensitive electronics unless the OEM procedure explicitly permits it.

* Use approved PPE and high-voltage isolation procedures whenever physical work on HV components is required.

* Preserve the original scan report before clearing faults.

### Key technical understanding

The purpose of a complete vehicle health scan is to establish a reliable electronic picture of the entire vehicle.

The technician must distinguish between:

* A genuine component fault.

* A power supply or ground fault.

* A network communication fault.

* A module that is not fitted.

* A security or diagnostic access restriction.

This distinction prevents unnecessary ECU replacement and helps identify the actual root cause.

---

### Module 1 — Professional Diagnostic Scanner Operation

### Lesson 1.5: Diagnostic Trouble Code Retrieval and Interpretation

A Diagnostic Trouble Code (DTC) is a standardized or manufacturer-defined identifier stored by a vehicle control module when it detects an abnormal operating condition.

For an EV technician, DTC interpretation is one of the most important diagnostic skills. A DTC identifies a detected problem or abnormal condition, but it does not automatically identify the component that must be replaced.

For example, a battery-management DTC may indicate abnormal cell voltage. The underlying cause could be:

* A genuinely degraded cell.

* A poor electrical connection.

* A voltage-sensing circuit fault.

* A wiring or connector problem.

* An internal BMS measurement fault.

The technician must interpret the code in its operating context and establish the root cause through testing.

This lesson follows the four sections in your handbook.

### 1.5.1 Stored, Pending and Permanent DTCs

These three DTC categories describe different stages or conditions of fault detection and storage.

### A. Stored DTC

A stored DTC is a fault code that has been recorded by a control module after its diagnostic monitoring logic has met the required fault-detection criteria.

Depending on the vehicle and diagnostic system, the fault may still be present or may have occurred previously.

Example:

A BMS detects a cell-voltage measurement outside its permitted range and records a DTC.

The scanner may display:

| Parameter   | Illustrative result                                                        |
| ----------- | -------------------------------------------------------------------------- |
| Module      | BMS                                                                        |
| DTC         | P0A80                                                                      |
| Description | Replace hybrid/EV battery pack (generic description; applicability varies) |
| Status      | Stored                                                                     |

The code does not prove that the battery pack must be replaced. Further diagnosis is necessary.

### B. Pending DTC

A pending DTC indicates that a diagnostic monitor has detected a fault condition, but the requirements for confirming or storing it as a mature fault have not necessarily been met.

For example:

* A sensor signal becomes abnormal.

* The ECU detects the abnormal condition.

* The monitor records a pending fault.

* The fault may be confirmed if the required detection conditions occur again.

The exact confirmation logic depends on the manufacturer's diagnostic strategy.

Why pending codes matter

Pending DTCs can help identify intermittent faults before they become confirmed faults.

A technician should not ignore them simply because the warning light is not illuminated.

### C. Permanent DTC

A permanent DTC is a code that cannot normally be erased using a conventional scan-tool clear command or by disconnecting the battery.

It is commonly associated with emissions-related OBD monitoring requirements.

The relevant ECU removes the permanent DTC after the prescribed diagnostic monitor has successfully completed and the system determines that the fault has been corrected.

Important distinction: Permanent DTC behavior is governed by the applicable OBD implementation. Do not assume every manufacturer-specific EV fault uses permanent-DTC logic.

### Comparison

| Characteristic             | Stored                              | Pending                             | Permanent                                |
| -------------------------- | ----------------------------------- | ----------------------------------- | ---------------------------------------- |
| Fault detected             | Yes                                 | Yes                                 | Previously confirmed                     |
| Confirmation requirements  | Met according to monitor logic      | Not necessarily met                 | Previously met                           |
| Conventional clear command | Usually possible, subject to system | Usually possible, subject to system | Normally cannot directly erase           |
| Automatic removal          | Depends on ECU logic                | Depends on monitor results          | After prescribed successful monitoring   |
| Diagnostic importance      | High                                | Important for intermittent faults   | Evidence of a previously confirmed fault |

### 1.5.2 Active and Historical Faults

Stored, pending and permanent describe DTC categories. Active and historical describe the fault's current or previous occurrence status.

These terms are not necessarily displayed identically across all manufacturers.

### A. Active fault

An active fault is a fault condition that is currently detected or remains present according to the ECU's diagnostic logic.

Example:

An inverter temperature sensor circuit has an open circuit.

The inverter controller continuously monitors the sensor input and detects that its signal is outside the expected electrical range.

The scanner may display:

* DTC: Sensor circuit fault.

* Status: Current or active.

* System: Inverter controller.

* Operating condition: READY, depending on the vehicle and fault.

The technician should investigate the sensor circuit, connector, wiring, reference supply and ground according to the manufacturer's wiring diagram.

### B. Historical fault

A historical fault is a fault that occurred previously but is not currently detected.

Example:

A vehicle experienced a temporary low-voltage supply condition during startup.

The VCU recorded a communication-related DTC. After the 12 V supply recovered, communication returned to normal.

The fault may remain in memory as historical.

### Active versus historical

| Feature                 | Active                               | Historical                                     |
| ----------------------- | ------------------------------------ | ---------------------------------------------- |
| Present fault condition | Currently detected                   | Not currently detected                         |
| Diagnostic priority     | Usually high                         | Depends on severity and recurrence             |
| Investigation           | Check current conditions             | Investigate occurrence history                 |
| Possible cause          | Current circuit or component problem | Intermittent or previously corrected condition |

### Workshop example: Intermittent CAN communication fault

Imagine that the VCU records a communication fault with the BMS.

At the time of inspection:

* VCU communication: Available.

* BMS communication: Available.

* Communication DTC: Historical.

* Current vehicle operation: Normal.

Do not immediately replace the BMS.

Investigate:

* Whether the fault repeatedly returns.

* Whether the 12 V supply experienced a previous voltage drop.

* Whether the CAN network has intermittent wiring or connector problems.

* Whether other ECUs recorded related communication faults.

* Whether the fault occurred during a particular operating condition.

The objective is to identify the circumstances that caused the original communication loss.

### 1.5.3 Manufacturer-Specific Descriptions

DTCs are not always interpreted correctly using a generic code description.

There are two important categories:

Generic DTCs

These use standardized diagnostic definitions where applicable. They are commonly associated with OBD-II/EOBD systems.

Manufacturer-specific DTCs

These are defined or interpreted according to the vehicle manufacturer's diagnostic strategy. Their descriptions, failure conditions and diagnostic procedures may differ between manufacturers.

### Example of DTC structure

A five-character powertrain DTC commonly follows this structure:

### Example: P0A80

### P

System category

### 0

Generic / standardized

### A

Fault grouping

### 8

Fault identification

### 0

Fault identification

Simplified structural illustration. Exact DTC interpretation must be checked against the applicable standard and OEM information.

The first character identifies the general system category:

| First character | System                |
| --------------- | --------------------- |
| P               | Powertrain            |
| B               | Body                  |
| C               | Chassis               |
| U               | Network communication |

The second character commonly indicates whether the code is generic or manufacturer-controlled within the relevant DTC family.

### Why generic descriptions can mislead EV technicians

Consider a scanner displaying a battery-related DTC.

A generic scanner may provide only a short description. An OEM diagnostic system may provide additional information, including:

* Exact failure subtype.

* Detection conditions.

* Affected battery section or circuit.

* Associated DTCs.

* Required live-data parameters.

* Manufacturer diagnostic test procedure.

* Repair and verification instructions.

Professional rule: Use the generic description as an initial reference, not as the final diagnosis.

For EV and hybrid systems, confirm the exact code against manufacturer service information for the specific vehicle, model year and software configuration.

### 1.5.4 DTC Priority and Fault Relationships

A vehicle can record several DTCs at the same time.

The technician must determine which code represents the primary fault and which codes may be consequences of that fault.

This is particularly important in EVs because multiple control modules depend on shared power supplies and communication networks.

### A. DTC priority

A useful diagnostic priority assessment considers:

* Safety implications.

* Whether the fault is currently active.

* Whether the fault affects vehicle operation.

* Whether the fault causes other systems to shut down.

* Whether the fault is supported by additional evidence.

* Whether the manufacturer identifies a priority diagnostic procedure.

For example, an HV isolation fault may require immediate attention because of the potential electrical safety implications.

A minor body-control communication fault may have a lower operational priority.

However, never assume that a code is low priority simply because the vehicle still drives.

### B. Primary and secondary DTCs

A primary DTC represents the original fault or condition responsible for a group of symptoms.

A secondary DTC may be generated because another system is no longer receiving the expected signal or message.

Example: Simulated EV diagnostic case

A vehicle reports three faults:

| Module             | DTC description                    | Status |
| ------------------ | ---------------------------------- | ------ |
| BMS                | Battery communication interruption | Active |
| VCU                | BMS message missing                | Active |
| Instrument cluster | Powertrain warning message         | Active |

A possible relationship is:

Possible primary fault

BMS communication interruption

Secondary consequence

VCU does not receive expected BMS messages

Driver notification

Instrument cluster displays powertrain warning

This is a possible fault relationship, not proof of the actual cause.

The BMS itself may have lost power, the network may have failed, or a gateway may be preventing communication.

The technician must test the actual system.

### C. How to establish DTC relationships

Use this diagnostic approach:

Step 1 — Retrieve all DTCs

Perform a full-system scan rather than relying on one ECU.

Step 2 — Record fault status

Identify active, stored, pending and historical information as supported by the scanner.

Step 3 — Compare affected modules

Look for faults that appear across multiple ECUs.

Step 4 — Identify shared dependencies

Check common power supplies, grounds, network connections and shared sensor signals.

Step 5 — Establish the sequence

Use timestamps, freeze-frame information and available event records to establish which fault occurred first. These records may not be available on every vehicle.

Step 6 — Test the suspected root cause

Use OEM procedures, wiring diagrams, live data and appropriate electrical measurements.

Step 7 — Verify the repair

Repeat the scan and confirm that the original fault does not return under the relevant test conditions.

### Professional diagnostic example: Multiple DTCs

Simulated training data

A hybrid vehicle arrives with a powertrain warning.

A complete scan produces:

| ECU                | DTC                              | Status |
| ------------------ | -------------------------------- | ------ |
| BMS                | Battery voltage monitoring fault | Active |
| VCU                | Battery data invalid             | Active |
| Inverter           | Torque limitation request        | Stored |
| Instrument cluster | Powertrain warning               | Active |

A weak diagnostic approach would be to replace the battery, VCU and inverter.

A professional approach is different:

* Investigate the BMS voltage-monitoring fault first.

* Check whether the VCU's invalid battery data is a consequence of the BMS fault.

* Determine whether inverter torque limitation resulted from unavailable battery information.

* Examine the OEM-defined battery monitoring data and related electrical circuits.

* Confirm the root cause before replacing any component.

This is the difference between code replacement and evidence-based diagnosis.

### Key workshop principles

* A DTC identifies a detected condition, not necessarily a failed component.

* Pending faults can reveal intermittent problems.

* Permanent DTCs follow specific monitoring and clearing requirements.

* Active and historical status must be interpreted separately from DTC category.

* Generic descriptions may not provide enough information for EV diagnosis.

* Multiple DTCs can share one underlying cause.

* Always preserve the original scan before clearing codes.

* Verify repairs using the manufacturer's specified test procedure.

---

### Module 1 — Professional Diagnostic Scanner Operation

### Lesson 1.6: Freeze-Frame and Live Data Analysis

The purpose of this lesson is to teach you how to use diagnostic data to identify what happened when a fault occurred, what is happening now, and how to distinguish a genuine component failure from a sensor or electrical circuit problem.

### 1.6.1 Freeze-Frame Data

Freeze-frame data is a recorded snapshot of selected operating parameters when an ECU detects a fault under the applicable monitoring conditions.

It helps establish the conditions under which the fault occurred.

Typical recorded parameters include:

* Battery voltage.

* Vehicle speed.

* Battery current.

* Motor speed.

* Coolant temperature.

* Accelerator position.

* Charging status.

* Sensor measurements.

Example: Battery temperature fault

Simulated diagnostic data

| Parameter                   | Recorded value |
| --------------------------- | -------------- |
| Maximum battery temperature | 54°C           |
| Minimum battery temperature | 31°C           |
| Vehicle speed               | 0 km/h         |
| Charging status             | Charging       |
| Battery current             | 42 A           |
| Pack voltage                | 386 V          |

Temperature difference:

`ΔT = T_max − T_min = 54 − 31 = 23 °C`

The battery had a recorded temperature spread of 23°C.

Technician interpretation:

The fault occurred while the vehicle was stationary and charging. Investigate temperature-sensor accuracy, coolant circulation and thermal-management operation.

Do not conclude that the battery is defective from this snapshot alone.

### 1.6.2 Live Data Parameters

Live data consists of measurements and calculated values communicated by vehicle ECUs while the vehicle is operating.

It helps the technician monitor system behavior in real time or near real time.

Important EV parameters include:

| System         | Parameter           | Purpose                          |
| -------------- | ------------------- | -------------------------------- |
| BMS            | Pack voltage        | Monitor total battery voltage    |
| BMS            | Cell voltage        | Identify cell voltage deviations |
| BMS            | Battery current     | Monitor charge/discharge current |
| BMS            | SoC                 | Estimate remaining charge        |
| BMS            | SoH                 | Estimate battery condition       |
| Inverter       | DC-link voltage     | Monitor inverter DC supply       |
| Motor          | Motor speed         | Monitor rotational speed         |
| DC-DC          | Output voltage      | Monitor low-voltage supply       |
| Thermal system | Coolant temperature | Monitor cooling performance      |
| OBC            | Charging current    | Monitor AC charging operation    |

### Important engineering calculations

Battery pack voltage

For series-connected cell groups:

`V_pack = Σ V_cell groups`

If 96 series-connected groups each measure 4.0 V:

`V_pack = 96 × 4.0 V = 384 V`

Cell voltage deviation

Suppose the BMS reports:

| Cell group | Voltage |
| ---------- | ------- |
| 1          | 3.72 V  |
| 2          | 3.73 V  |
| 3          | 3.71 V  |
| 4          | 3.52 V  |

`ΔV = V_max − V_min = 3.73 − 3.52 = 0.21 V`

The deviation is 210 mV. Its significance must be evaluated against OEM limits, battery chemistry, temperature, SoC and load conditions.

### 1.6.3 Sensor Values and Operating Conditions

An ECU depends on sensor information to control vehicle systems.

A sensor reading must always be interpreted in relation to the operating condition.

### A. Temperature sensors

Many automotive temperature sensors use NTC thermistors.

An NTC thermistor has:

* Higher resistance at lower temperature.

* Lower resistance at higher temperature.

Example:

| Sensor           | Reading |
| ---------------- | ------- |
| Battery sensor 1 | 28°C    |
| Battery sensor 2 | 29°C    |
| Battery sensor 3 | -40°C   |

A -40°C reading may indicate an open circuit on some systems. Confirm the manufacturer's diagnostic criteria before deciding.

### B. Voltage sensors

Voltage measurements are used to monitor:

* Battery pack voltage.

* Cell-group voltage.

* DC-link voltage.

* 12 V auxiliary supply.

An abnormal reading may result from a genuine electrical condition, a poor connection, wiring damage or a measurement-circuit fault.

### C. Current sensors

Current measurement systems may use Hall-effect sensors or shunt resistors.

They help the BMS monitor current entering and leaving the battery.

Always confirm whether the manufacturer's data convention uses positive current for charging or discharging.

### D. Operating conditions to record

When investigating abnormal data, record:

* Vehicle operating mode.

* Ambient temperature.

* Battery SoC.

* Charging or driving status.

* Electrical load.

* Coolant-system status.

* Time since shutdown, where relevant.

Key principle: A sensor reading cannot be judged accurately without understanding the conditions under which it was measured.

### 1.6.4 Data Graphing and Recording

A graph shows how a parameter changes over time.

This is useful for identifying intermittent faults, sudden voltage drops, unstable sensors and temperature trends.

### Example: Battery temperature trend

Simulated data

| Time   | Temperature |
| ------ | ----------- |
| 0 min  | 28°C        |
| 5 min  | 30°C        |
| 10 min | 34°C        |
| 15 min | 39°C        |
| 20 min | 46°C        |
| 25 min | 52°C        |

The graph shows a continuous increase.

Investigate:

* Coolant circulation.

* Pump operation.

* Heat exchanger performance.

* Temperature sensor accuracy.

* Thermal-management control strategy.

### Recording live data

During an approved diagnostic test, record relevant parameters together.

For example:

* Battery voltage.

* Battery current.

* Cell voltages.

* Motor speed.

* Inverter temperature.

* Battery temperature.

* Vehicle speed.

This allows the technician to correlate different measurements and identify when the fault occurs.

Sampling limitation: A scan tool may refresh too slowly to capture fast electrical transients. Use an appropriate oscilloscope when higher sampling speed or waveform detail is required.

### 1.6.5 Abnormal Reading Interpretation

An abnormal reading is a value that falls outside the expected range or conflicts with other measurements.

It does not automatically mean that the sensor is defective.

### Example A: Implausible temperature

| Parameter            | Reading |
| -------------------- | ------- |
| Temperature sensor 1 | 27°C    |
| Temperature sensor 2 | 28°C    |
| Temperature sensor 3 | 27°C    |
| Temperature sensor 4 | 150°C   |

Possible causes:

* Sensor failure.

* Short circuit.

* Damaged wiring.

* Connector corrosion.

* Incorrect reference voltage.

* ECU measurement fault.

* Genuine abnormal temperature.

The technician must establish whether the reading represents a real physical condition or an electrical measurement error.

### Example B: Abnormal battery voltage

A BMS reports one cell group significantly lower than the others.

Possible causes:

* Cell degradation.

* High internal resistance.

* Interconnection resistance.

* Voltage-sensing harness fault.

* BMS measurement-channel fault.

Compare the data under suitable conditions and follow the OEM diagnostic procedure.

### Example C: Abnormal current

A vehicle appears inactive, but the current sensor reports significant current.

Possible explanations:

* An auxiliary electrical load is operating.

* The vehicle is not actually in the assumed operating state.

* Current-sensor offset.

* Sensor calibration issue.

* BMS measurement fault.

Confirm the vehicle's electrical state before interpreting the reading.

### Professional workshop case study

Simulated diagnostic case

Customer complaint: Battery temperature warning during charging.

Initial scan:

| Parameter         | Result                       |
| ----------------- | ---------------------------- |
| ECU               | BMS                          |
| DTC               | Battery temperature abnormal |
| Status            | Active                       |
| Vehicle condition | Charging                     |

Live data:

| Parameter            | Reading |
| -------------------- | ------- |
| Temperature sensor 1 | 31°C    |
| Temperature sensor 2 | 32°C    |
| Temperature sensor 3 | 33°C    |
| Temperature sensor 4 | 68°C    |
| Pump command         | 75%     |
| Pump actual speed    | 0 RPM   |

Professional interpretation

Two abnormalities require investigation:

* Sensor 4 reports a much higher temperature than the other sensors.

* The coolant pump is commanded to operate, but reported speed is zero.

Possible fault paths include a genuine localized temperature increase, a sensor circuit problem, a pump electrical fault or a feedback fault.

Diagnostic procedure:

* Save the original DTC and freeze-frame information.

* Check the OEM temperature limits and plausibility criteria.

* Inspect the temperature sensor circuit.

* Verify pump supply, ground, control and feedback circuits.

* Check coolant circulation using the approved procedure.

* Recheck live data after repair.

* Perform a final scan and verify charging operation.

Do not replace the battery pack based only on these readings.

### Final technical points

* Freeze-frame data explains the conditions associated with a fault.

* Live data shows current or near-current measurements.

* Sensor values must be compared with OEM specifications.

* Graphs help identify trends and intermittent problems.

* A scan-tool reading is not always sufficient to diagnose a fast electrical fault.

* An abnormal sensor value may originate from the sensor, wiring, ECU or genuine physical condition.

---

### Module 1 — Professional Diagnostic Scanner Operation

### Lesson 1.7: Active Tests and Bidirectional Controls

This lesson covers how a professional diagnostic scanner can do more than read faults and display sensor data: it can send commands to vehicle control modules and observe how the vehicle responds.

The five sections are:

* Active test principles

* Actuator command testing

* Pump, fan and relay activation

* Commanded versus actual values

* Safety limitations

### 1.7.1 Active Test Principles

An active test is a diagnostic function in which a scan tool requests an ECU to operate or change the state of a specific component.

Unlike ordinary live-data monitoring, active testing involves sending a command to the vehicle.

For example, a technician can use a compatible diagnostic scanner to request:

* Battery coolant pump activation.

* Radiator cooling fan operation.

* Cooling-system valve movement.

* Relay activation.

* Electric water pump speed adjustment.

* Certain actuator positions.

### How an active test works

1\. Diagnostic scanner

Technician selects an available active test

2\. ECU receives command

Checks operating conditions and safety permissions

3\. Output driver operates actuator

ECU controls the relevant electrical output

4\. Actual response is monitored

Scanner displays feedback or measured operating values

Important: A successful command does not prove that the component is mechanically or electrically healthy. The technician must verify the actual response.

### 1.7.2 Actuator Command Testing

An actuator converts an electrical control signal into a physical action.

Examples in EV and hybrid vehicles include:

| Actuator                     | Function                                                 |
| ---------------------------- | -------------------------------------------------------- |
| Electric coolant pump        | Circulates coolant                                       |
| Cooling fan                  | Moves air through a heat exchanger                       |
| Electronic coolant valve     | Controls coolant flow direction                          |
| Battery contactor            | Connects or disconnects the HV battery under ECU control |
| Electric compressor          | Provides refrigerant compression                         |
| Electronic throttle actuator | Controls throttle plate position in applicable hybrids   |

### Example: Electric coolant pump

A diagnostic scanner may provide a pump activation command.

Simulated diagnostic results:

| Parameter            | Reading     |
| -------------------- | ----------- |
| Requested pump speed | 3,000 RPM   |
| Actual pump speed    | 0 RPM       |
| Pump command status  | Active      |
| Pump feedback        | No response |

Possible fault areas:

* Missing electrical supply.

* Poor ground connection.

* Open or shorted wiring.

* Pump motor failure.

* ECU output-stage fault.

* Communication or feedback circuit fault.

### Technician's diagnostic logic

Do not immediately replace the pump.

First establish whether the ECU is issuing the command, whether the electrical circuit responds and whether the pump produces the expected physical output.

### 1.7.3 Pump, Fan and Relay Activation

These are common active tests during EV thermal-management and low-voltage electrical diagnosis.

### A. Electric coolant pump activation

Purpose:

* Verify pump operation.

* Check speed feedback.

* Investigate coolant circulation problems.

* Confirm response to ECU commands.

Observe:

* Requested speed.

* Actual speed.

* Current consumption, if available.

* Pump feedback status.

* Coolant temperature response.

A pump reporting zero RPM despite an activation command requires further investigation.

### B. Cooling fan activation

Purpose:

* Verify fan motor operation.

* Check fan control circuits.

* Confirm variable-speed control.

* Investigate overheating or thermal derating.

Simulated test:

| Parameter          | Result    |
| ------------------ | --------- |
| Fan requested duty | 70%       |
| Fan actual duty    | 70%       |
| Fan speed          | 1,800 RPM |
| Fan status         | Operating |

The response appears consistent, but airflow and physical fan operation should also be checked.

### C. Relay activation

Relays are electrically controlled switches used in vehicle electrical systems.

A compatible active test may command a relay ON or OFF.

A technician should investigate:

* Relay control signal.

* Coil supply and ground.

* Contact operation.

* Voltage drop across the contacts under suitable load.

* Wiring and connector condition.

A relay clicking does not necessarily prove that its contacts can carry the required current.

High-voltage contactor warning: HV contactors are not ordinary 12 V relays. Never manually energize, bypass or force an HV contactor. Follow the manufacturer's diagnostic and isolation procedures.

### 1.7.4 Commanded Versus Actual Values

One of the most important skills in bidirectional diagnosis is comparing the requested operation with the actual response.

* Commanded value: What the ECU requests.

* Actual value: What the system reports or measures as happening.

Example:

| Parameter              | Commanded | Actual |
| ---------------------- | --------- | ------ |
| Coolant pump speed     | 3,000 RPM | 0 RPM  |
| Cooling fan duty       | 70%       | 68%    |
| Coolant valve position | 80%       | 80%    |

Interpretation:

* The pump has a command-response discrepancy.

* The fan response is close to the requested duty.

* The coolant valve position agrees with the requested position, assuming the feedback is valid.

### Understanding the discrepancy

For a speed-controlled actuator:

`Speed error = N_commanded − N_actual`

For the pump:

`3,000 − 0 = 3,000 RPM`

This is a substantial discrepancy.

However, the calculation alone does not identify the failed component. You must verify the feedback signal and electrical circuit.

### Diagnostic decision sequence

* Confirm that the correct actuator was selected.

* Check whether the ECU accepted the command.

* Confirm that the operating conditions permit activation.

* Observe the electrical output and feedback data available.

* Inspect the actuator circuit using the OEM procedure.

* Confirm physical operation.

* Repeat the test after repair.

### 1.7.5 Safety Limitations

Active tests can cause physical movement, electrical switching, heat generation or unexpected changes in vehicle operating state.

They must be performed under controlled workshop conditions.

Essential precautions:

* Confirm vehicle identity and the correct ECU.

* Read relevant DTCs before testing.

* Follow the OEM test procedure.

* Secure the vehicle against unintended movement.

* Keep hands and tools clear of fans, pumps and moving components.

* Ensure coolant and refrigerant systems are operated within approved conditions.

* Use appropriate PPE and approved test equipment.

* Never bypass an interlock or safety protection.

* Never force contactors or energize HV circuits manually.

* Stop immediately if abnormal noise, overheating, leakage or unexpected movement occurs.

High-voltage safety

An active test is not permission to work on exposed HV components. HV isolation, verification of absence of voltage and all other required safety procedures must follow the vehicle manufacturer's instructions and the technician's authorization level.

### Professional workshop case study

Customer complaint: Battery temperature warning appears during charging.

The technician connects an approved diagnostic scanner and retrieves the following simulated data:

| Parameter            | Reading   |
| -------------------- | --------- |
| Battery temperature  | 45°C      |
| Coolant pump command | 80%       |
| Pump actual speed    | 0 RPM     |
| Cooling fan command  | 60%       |
| Fan actual speed     | 1,500 RPM |

Initial interpretation:

* The battery temperature is elevated and must be assessed against OEM limits.

* The pump has no reported speed response.

* The fan appears to be operating.

Diagnostic approach:

* Save DTCs and freeze-frame data.

* Confirm whether the ECU permits pump activation.

* Perform the approved pump active test.

* Check the pump's electrical supply, ground and control circuit according to OEM instructions.

* Verify feedback and physical coolant circulation.

* Repair the confirmed fault.

* Repeat the active test and monitor battery temperatures under approved conditions.

The pump must not be condemned until its electrical supply, control and feedback have been properly assessed.

### Key technician takeaways

* Active tests send commands to vehicle ECUs.

* Bidirectional control allows the scanner to request actuator operation.

* Commanded and actual values must be compared.

* A command being accepted does not prove successful actuator operation.

* Electrical measurements and physical verification are essential.

* OEM safety procedures always take priority.

---

### Module 1 — Professional Diagnostic Scanner Operation

### Lesson 1.8: Special Functions and Service Operations

A professional diagnostic scanner does more than retrieve DTCs, display live data and activate actuators. It can also perform service operations that change ECU settings, erase maintenance information, initialize replacement components and recalibrate electronic systems.

These operations are important after repairs, component replacement and certain maintenance procedures.

This lesson follows the five sections in your official handbook.

### 1.8.1 Service Resets

A service reset is a diagnostic operation that clears or updates specific maintenance-related information stored in a vehicle control module.

It does not necessarily repair a fault. It updates the vehicle's service records or resets a maintenance counter after the relevant work has been completed.

### Common service resets

| Service reset              | Purpose                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------- |
| Oil service reset          | Resets the engine oil maintenance interval in applicable vehicles                     |
| Brake service reset        | Updates brake maintenance information where supported                                 |
| Battery replacement reset  | Registers or resets battery-monitoring information                                    |
| Maintenance interval reset | Restarts a scheduled service counter                                                  |
| TPMS reset                 | Initiates or updates tire-pressure monitoring procedures, depending on vehicle design |
| DPF service reset          | Resets applicable diesel particulate filter service information                       |

### EV and hybrid examples

12 V auxiliary battery replacement

Some vehicles use a battery monitoring system to track battery condition, charging behavior and aging.

After replacing the 12 V battery, an OEM procedure may require battery registration or adaptation.

Why?

The energy-management system may need to recognize the new battery and update its charging strategy.

Important: Not every vehicle requires battery registration. Always check the manufacturer's service information.

### Professional procedure

* Confirm vehicle identification.

* Confirm the maintenance or repair has been completed.

* Connect the correct diagnostic scanner.

* Select the relevant ECU and service function.

* Check the displayed conditions and warnings.

* Execute the reset according to OEM instructions.

* Verify that the reset was accepted.

* Save the diagnostic report.

Never reset maintenance data merely to make a warning disappear without completing the required work.

### 1.8.2 Adaptations and Relearning

Adaptation is a process in which an ECU stores or updates learned values to compensate for component variation, wear, operating conditions or replacement parts.

These learned values help the control system operate accurately.

### Why adaptations are necessary

Electronic control systems cannot always assume that every replacement component has exactly the same characteristics as the original.

For example:

* A new sensor may have a slightly different offset.

* A throttle body may require position learning.

* A transmission may need clutch adaptation.

* An electric motor control system may require position-related learning.

### Examples of adaptations

| System              | Adaptation or relearning                  |
| ------------------- | ----------------------------------------- |
| Electronic throttle | Throttle position relearning              |
| Transmission        | Clutch or shift adaptation                |
| Battery monitoring  | Battery condition or sensor adaptation    |
| Steering system     | Steering angle relearning                 |
| Motor control       | Position-related learning where specified |
| HVAC system         | Air-mix actuator relearning               |

### Example: Electronic throttle adaptation

An electronic throttle body contains an electric actuator and position sensors.

After replacement or certain repairs, the ECU may need to relearn the throttle's reference positions.

A typical conceptual process is:

* Confirm correct installation.

* Confirm electrical connections.

* Connect the OEM-compatible diagnostic tool.

* Select throttle adaptation.

* Meet the specified ignition, voltage and temperature conditions.

* Execute the relearning procedure.

* Confirm successful completion.

* Check throttle position data and relevant DTCs.

The actual procedure varies by manufacturer.

### Adaptation versus programming

These terms must not be confused.

| Adaptation                            | Programming                                          |
| ------------------------------------- | ---------------------------------------------------- |
| Updates learned operating values      | Installs or changes ECU software or calibration      |
| Often follows component replacement   | Often follows software updates or module replacement |
| Usually does not replace the firmware | May change firmware or calibration data              |
| Example: throttle relearning          | Example: ECU firmware flashing                       |

An ECU can have correct firmware but incorrect or incomplete adaptations.

### 1.8.3 Component Initialization

Component initialization is a diagnostic procedure that prepares a newly installed or replacement component for operation by the vehicle's control system.

It may establish reference positions, identify the component, configure initial operating conditions or synchronize it with another module.

### Components that may require initialization

| Component                 | Possible initialization requirement           |
| ------------------------- | --------------------------------------------- |
| Electric steering system  | Steering reference or position initialization |
| ABS module                | Configuration or initialization               |
| Electronic parking brake  | Actuator initialization                       |
| Battery management system | Replacement battery or module initialization  |
| Electric coolant valve    | Reference-position initialization             |
| HVAC actuator             | End-stop or position initialization           |

### Example: Electric coolant valve

An electric coolant valve controls coolant flow between different thermal circuits.

After replacing a valve, an OEM procedure may require initialization.

The control module may need to establish:

* The valve's reference position.

* Its available movement range.

* Position-feedback correlation.

* Correct communication with the actuator.

### What happens if initialization is skipped?

Possible symptoms include:

* Incorrect coolant routing.

* Cooling or heating performance problems.

* Unexpected actuator behavior.

* DTCs related to position or initialization.

* Thermal-management limitations.

The precise effects depend on the vehicle's design.

### Technician's procedure

* Verify the correct replacement part.

* Inspect installation and connectors.

* Confirm the required supply voltage.

* Select the relevant initialization function.

* Follow the displayed OEM conditions.

* Allow the procedure to complete without interruption.

* Verify position feedback and system operation.

### 1.8.4 Calibration Functions

Calibration establishes or adjusts the relationship between a measured value, a reference position or an electronic control system's expected operating condition.

It is particularly important where accurate sensor measurements and component positioning are essential.

### Common calibration functions

| Calibration                     | Purpose                                               |
| ------------------------------- | ----------------------------------------------------- |
| Steering angle calibration      | Establishes the steering angle reference              |
| Yaw-rate sensor calibration     | Establishes the required reference condition          |
| Acceleration sensor calibration | Establishes a reference for acceleration measurements |
| Camera calibration              | Aligns camera measurements with vehicle geometry      |
| Radar calibration               | Establishes correct radar alignment                   |
| Pressure sensor calibration     | Applies the specified reference procedure             |
| Motor position calibration      | Establishes motor position information where required |

### Example: Steering angle sensor calibration

The steering angle sensor reports steering-wheel position to vehicle control systems.

This information may be used by:

* Electronic stability control.

* ABS.

* Electric power steering.

* Advanced driver assistance systems.

If the reference position is incorrect, the ECU may interpret straight-ahead driving as a steering input.

A calibration procedure may require:

* Correct wheel alignment and steering geometry.

* Steering wheel positioned as specified.

* Vehicle on the required level surface.

* Correct tire pressures.

* Stable electrical supply.

* Execution of the OEM calibration function.

* Verification of steering angle data and DTC status.

Important distinction: Calibration cannot correct a mechanically misaligned steering system or a damaged sensor. Correct mechanical condition must be established first.

### Calibration versus adaptation versus initialization

| Operation      | Main purpose                                               |
| -------------- | ---------------------------------------------------------- |
| Adaptation     | Learns or updates operating values                         |
| Initialization | Prepares a component for operation                         |
| Calibration    | Establishes or adjusts a measurement or position reference |

Some manufacturers use these terms differently. The diagnostic function's actual purpose and OEM instructions take priority over its menu label.

### 1.8.5 Electronic Parking Brake Service Modes

An electronic parking brake (EPB) uses electrical actuators and an electronic control system to apply and release the parking brake.

Unlike a conventional handbrake cable, the system may use electric motors integrated into the rear brake calipers or a separate actuator mechanism.

### Why EPB service mode is required

During rear brake pad replacement, the parking brake actuator may need to retract to create sufficient clearance for the new pads.

The diagnostic scanner can provide a dedicated service function on supported vehicles.

Common functions include:

* Enter brake pad replacement mode.

* Retract parking brake actuator.

* Release EPB.

* Exit service mode.

* Close or initialize the actuator.

* Perform required post-service checks.

### General EPB service procedure

Follow vehicle-specific OEM instructions

Stage 1 — Preparation

* Identify the vehicle and EPB system.

* Check relevant DTCs.

* Confirm the correct brake service procedure.

* Secure the vehicle against movement.

* Maintain the required 12 V supply condition.

Stage 2 — Enter service mode

* Connect the compatible diagnostic scanner.

* Select the EPB control module.

* Choose the brake pad replacement or maintenance function.

* Follow the displayed instructions.

* Confirm that the actuators have entered the required service position.

Stage 3 — Mechanical service

Carry out the brake service using the manufacturer's mechanical procedure and appropriate equipment.

Stage 4 — Exit service mode

* Reinstall the components correctly.

* Select the EPB closing or exit-service-mode function.

* Allow the actuator procedure to complete.

* Perform any required initialization or calibration.

* Check for DTCs.

* Verify parking brake application and release according to OEM instructions.

Critical warning: Never force an EPB actuator or attempt to rotate an integrated electric motor mechanism without confirming the correct mechanical procedure. Some systems can be damaged by incorrect manual retraction.

### Professional workshop case study

Vehicle: Electric vehicle with rear electronic parking brake.

Customer complaint: Rear brake pads have been replaced, but the parking brake warning remains illuminated.

Simulated diagnostic scan:

| Parameter            | Result              |
| -------------------- | ------------------- |
| EPB module           | Communicating       |
| Parking brake status | Service mode active |
| Left actuator        | Retracted           |
| Right actuator       | Retracted           |
| Service procedure    | Not completed       |

### Technician's interpretation

The actuators have entered service mode, but the system has not completed the required closing procedure.

Possible causes include:

* Service mode was not exited.

* Initialization was not completed.

* An actuator position was not confirmed.

* An electrical or mechanical fault remains.

### Diagnostic approach

* Confirm that the brake assembly has been correctly installed.

* Inspect the actuator connectors and wiring.

* Review EPB live data and stored DTCs.

* Follow the OEM closing procedure.

* Complete any required initialization.

* Verify application and release.

* Perform a final scan and document the results.

Do not assume that clearing the warning lamp alone completes the repair.

### Key technician takeaways

* Service resets update maintenance-related information.

* Adaptations allow ECUs to learn or update operating values.

* Initialization prepares components for correct operation.

* Calibration establishes accurate reference values or positions.

* EPB service modes allow controlled brake actuator movement during maintenance.

* These functions must be performed using the correct vehicle-specific procedures.

---

### Module 1 — Professional Diagnostic Scanner Operation

### Lesson 1.9: Advanced Scanner Functions

At this level, a diagnostic scanner becomes more than a tool for reading fault codes. It becomes an advanced diagnostic platform that helps technicians follow manufacturer-defined procedures, access ECU configuration, identify software versions and manage diagnostic evidence.

This lesson covers the five official sections in your handbook.

### 1.9.1 Guided Diagnostics

Guided diagnostics is a scanner function that leads a technician through a structured fault-finding process.

Instead of simply displaying a DTC, the scanner may provide:

* Possible causes of the fault.

* Required preliminary checks.

* Wiring diagrams and connector information.

* Component test procedures.

* Expected measurement values.

* Decision steps based on test results.

Workshop example:

A vehicle reports:

Illustrative diagnostic example

Simulated data

### U0100

Lost Communication With ECM/PCM

Possible guided diagnostic sequence:

* Confirm the DTC and identify the reporting ECU.

* Check the vehicle battery and 12 V supply stability.

* Inspect relevant fuses and ECU power supplies.

* Check ground circuits.

* Inspect CAN-H and CAN-L wiring.

* Verify ECU communication and network condition.

Important: Guided diagnostics provides a test pathway, not proof of the failed component. You must verify each finding through measurements and physical inspection.

### 1.9.2 OEM Test Plans

OEM means Original Equipment Manufacturer.

An OEM test plan is a manufacturer-specific diagnostic procedure designed for a particular vehicle, ECU or fault condition.

It may contain:

* Preconditions for testing.

* Required scanner functions.

* Electrical measurement instructions.

* Connector and terminal references.

* Expected live-data values.

* Software-specific diagnostic routines.

* Pass/fail criteria.

Example: HV battery cooling system

An OEM test plan may instruct the technician to:

* Confirm the vehicle is in the required operating condition.

* Read battery temperature sensors.

* Command the cooling pump using an approved active test.

* Monitor commanded and actual pump operation.

* Check coolant flow and temperature response.

* Follow the manufacturer's fault-isolation procedure if the response is abnormal.

Technician's responsibility: Follow the correct vehicle-specific procedure. Do not substitute generic test values for OEM specifications.

### 1.9.3 ECU Coding and Configuration Access

ECU coding changes configurable software settings within an electronic control unit.

Configuration access allows a technician to inspect or modify supported vehicle settings.

Examples include:

* Vehicle equipment configuration.

* Battery type or capacity configuration, where supported.

* Installed control-unit configuration.

* Communication and network options.

* Market-specific equipment settings.

* Replacement ECU configuration.

### Coding versus programming

These operations are related but different.

| Operation          | Meaning                                      |
| ------------------ | -------------------------------------------- |
| ECU coding         | Changes configuration settings or options    |
| ECU programming    | Loads or updates ECU software                |
| ECU adaptation     | Learns or adjusts operating parameters       |
| ECU initialization | Establishes initial operating state or setup |

Workshop example: ECU replacement

Suppose a replacement body control module is installed.

The replacement ECU may require vehicle configuration so that it correctly recognizes the vehicle's installed equipment.

A technician may need to:

* Identify the replacement ECU.

* Confirm hardware and software compatibility.

* Retrieve the original configuration, if available.

* Access the OEM coding procedure.

* Apply the correct configuration.

* Verify ECU communication and system operation.

Critical caution

Incorrect coding can cause missing functions, communication faults or vehicle-system malfunctions. Never change unknown configuration values experimentally.

Some operations require OEM authorization, an online connection, security access or a controlled programming power supply.

### 1.9.4 Software Identification

Software identification allows a technician to determine which software and calibration versions are installed in an ECU.

Typical identification information includes:

| Parameter          | Technical meaning                                          |
| ------------------ | ---------------------------------------------------------- |
| ECU part number    | Hardware or assembly identification                        |
| Hardware number    | ECU hardware revision                                      |
| Software number    | Installed software identification                          |
| Calibration ID     | Engine, motor or system calibration identifier             |
| CVN                | Calibration Verification Number                            |
| Bootloader version | Software responsible for starting or updating ECU software |
| ECU serial number  | Individual unit identification                             |

### Why software identification matters

Consider an EV with intermittent inverter communication faults.

Two vehicles of the same model may have different ECU software versions.

The technician should establish:

* Whether the correct ECU software is installed.

* Whether the software version matches the vehicle specification.

* Whether an applicable manufacturer software update exists.

* Whether the ECU has been previously programmed.

* Whether the calibration is compatible with the installed hardware.

Important distinction: A newer software version is not automatically the correct version for every vehicle. Compatibility must be verified against manufacturer information.

### 1.9.5 Diagnostic Data Management

Diagnostic data management is the process of collecting, storing, organizing and reviewing information obtained during vehicle diagnosis.

It is important because professional diagnosis must be supported by evidence.

Typical diagnostic records include:

* Full vehicle health reports.

* ECU identification records.

* DTC reports.

* Freeze-frame data.

* Live-data recordings.

* Active-test results.

* Software identification records.

* Before-and-after repair reports.

### Example: Recording a battery-related fault

Illustrative diagnostic report

Vehicle system

HV Battery Management System

Fault code

P0A80

Description

Replace Hybrid Battery Pack

Pack voltage

198.4 V

Lowest block voltage

14.2 V

Highest block voltage

15.8 V

All readings are simulated

These readings illustrate report structure only. They are not evidence of an actual battery defect.

The technician should retain the original scan and compare it with the post-repair scan.

This helps establish whether:

* The original fault was present.

* The repair changed the relevant measurements.

* The DTC returned.

* Other faults appeared during verification.

### Professional data-management practices

* Save reports using a consistent vehicle identification method.

* Record VIN, mileage, date and diagnostic tool details.

* Preserve original scan data before clearing DTCs.

* Keep before-and-after reports.

* Do not alter recorded measurements.

* Protect customer and vehicle information.

* Follow the workshop's data-retention procedures.

### How the five advanced functions work together

1\. Guided diagnostics

Identifies the recommended diagnostic pathway

2\. OEM test plans

Provides manufacturer-specific testing procedures

3\. ECU coding and configuration

Allows authorized configuration operations

4\. Software identification

Confirms ECU hardware and software identity

5\. Diagnostic data management

Preserves evidence and supports repair verification

### Professional technician's key point

An advanced diagnostic scanner does not replace engineering judgment. It provides access to information, procedures and control functions. The technician must still establish the actual cause through verified measurements, correct technical procedures and post-repair testing.

---

### Module 1 — Professional Diagnostic Scanner Operation

### Lesson 1.10: Professional Scanner Diagnostic Cases

This lesson brings together the scanner skills from Lessons 1.1–1.9. The objective is to diagnose vehicles systematically, avoid unnecessary component replacement and produce evidence that supports the repair decision.

We will use workshop-style examples with clearly identified simulated data.

### 1.10.1 Initial Inspection and Scan

A professional diagnosis begins before connecting the scanner.

The first objective is to establish the vehicle's condition and preserve the original diagnostic information.

### Step 1 — Initial vehicle inspection

Record:

* VIN and vehicle model.

* Model year and powertrain type.

* Odometer reading.

* Customer-reported symptoms.

* Warning lights and messages.

* Recent repairs or component replacements.

* 12 V battery condition.

For an EV or hybrid, also establish whether there are visible signs of damage, coolant leakage, collision damage or other conditions that could affect high-voltage system safety.

Safety: Do not touch or disconnect high-voltage components during an ordinary scan. If there is suspected HV damage, follow the manufacturer's safety and isolation procedures before further work.

### Step 2 — Connect the diagnostic scanner

* Confirm the scanner supports the vehicle.

* Inspect the diagnostic connector.

* Connect the scanner using the correct interface.

* Switch the vehicle to the required ignition or diagnostic mode.

* Identify the vehicle using the correct VIN and configuration.

* Establish communication with the vehicle ECUs.

### Step 3 — Perform a complete vehicle scan

Do not restrict the initial scan to the engine ECU.

Depending on vehicle architecture, scan:

* Battery Management System (BMS).

* Vehicle Control Unit (VCU).

* Inverter or Motor Control Unit.

* Onboard Charger (OBC).

* DC-DC converter.

* ABS/ESC.

* Body Control Module (BCM).

* Thermal management controller.

* Charging control modules.

### Step 4 — Save the original report

Record DTC status, ECU communication status, freeze-frame data and relevant live data before clearing any codes.

### 1.10.2 Multiple ECU Fault Investigation

Modern EVs and hybrids contain multiple ECUs connected through communication networks. A fault in one system can create faults in several other systems.

The critical skill is distinguishing the root fault from secondary or consequential faults.

### Simulated workshop case

Vehicle complaint

EV displays a warning:

Electric powertrain system fault — reduced power.

Simulated DTC data

| ECU      | DTC   | Description                               |
| -------- | ----- | ----------------------------------------- |
| VCU      | U0100 | Lost communication with ECM/PCM           |
| Inverter | U0121 | Lost communication with ABS module        |
| BMS      | P0A1F | Battery energy control module performance |
| ABS      | U0100 | Lost communication with ECM/PCM           |

These codes do not establish four failed ECUs.

### Diagnostic approach

1\. Identify common relationships

Check whether the DTCs involve the same network, ECU or power supply.

2\. Identify communication failures

Determine which modules are communicating and which are not.

3\. Check shared electrical supplies

Inspect relevant 12 V battery supply circuits, fuses, grounds and ECU power feeds using the manufacturer's wiring diagrams.

4\. Investigate the communication network

Depending on the network architecture, inspect:

* CAN-H and CAN-L.

* Network connectors and junctions.

* Termination resistance, where applicable.

* Network waveform using an oscilloscope.

* Short circuits and open circuits.

5\. Establish the primary fault

Use test results to identify the original failure rather than replacing every ECU reporting a communication DTC.

Engineering principle: Multiple communication DTCs can originate from one failed power supply, ground connection, network branch or communication node.

### 1.10.3 Intermittent Fault Analysis

An intermittent fault occurs when a fault appears under certain conditions but disappears at other times.

These faults are particularly challenging because the vehicle may operate normally during workshop inspection.

### Common causes

* Loose connectors.

* Corroded terminals.

* Damaged wiring.

* Thermal expansion and contraction.

* Vibration-related connection failures.

* Moisture intrusion.

* Unstable electrical supply.

* Intermittent sensor signals.

### Diagnostic procedure

Step 1 — Retrieve historical information

Check stored and historical DTCs, freeze-frame records and fault occurrence information where supported.

Step 2 — Identify the operating conditions

Determine whether the fault occurs:

* During acceleration.

* During regenerative braking.

* When the vehicle is cold.

* After the vehicle warms up.

* During AC or DC charging.

* Over rough road surfaces.

Step 3 — Record live data

Select relevant parameters and record them over time.

For example, when investigating a temperature-sensor fault, record the sensor signal, reference voltage and related operating conditions where supported.

Step 4 — Perform controlled inspections

Inspect wiring and connectors. Use approved movement or vibration tests only where safe and permitted by the manufacturer.

Step 5 — Capture the fault

Use scanner recording, an oscilloscope or another suitable instrument to capture the abnormal event.

### Example: Intermittent sensor signal

Illustrative simulated values

| Operating condition | Sensor output |
| ------------------- | ------------- |
| Vehicle stationary  | 2.48 V        |
| Normal driving      | 2.51 V        |
| Vibration event     | 0.15 V        |
| After vibration     | 2.49 V        |

The sudden voltage drop may indicate an intermittent circuit problem, but the technician must verify the sensor, reference supply, ground and wiring before deciding which component has failed.

### 1.10.4 Evidence-Based Diagnosis

Evidence-based diagnosis means making repair decisions using measurable and repeatable technical evidence.

A DTC is an indication of a detected condition. It is not automatically proof that the named component is defective.

### Evidence hierarchy

| Evidence                | Diagnostic value                                   |
| ----------------------- | -------------------------------------------------- |
| DTC description         | Identifies the detected fault condition            |
| Freeze-frame data       | Shows conditions when the fault was recorded       |
| Live data               | Shows current system behaviour                     |
| Electrical measurements | Verifies voltage, resistance or current conditions |
| Oscilloscope capture    | Shows signal behaviour over time                   |
| Physical inspection     | Identifies visible damage or connection defects    |
| OEM test procedure      | Provides manufacturer-defined acceptance criteria  |

### Example: EV cooling pump fault

A scanner reports a cooling pump performance fault.

A weak diagnostic conclusion would be:

"The scanner reports a pump fault. Replace the pump."

A professional investigation would establish:

* Is the pump receiving its specified supply voltage?

* Is the ground circuit correct under load?

* Is the ECU commanding the pump?

* Is the pump drawing the expected current?

* Is the pump actually operating?

* Is coolant circulating correctly?

* Are there restrictions, air pockets or leaks?

* Does the system meet OEM performance criteria?

Only after these checks should the technician determine whether the pump, wiring, control circuit or another part of the cooling system is responsible.

### 1.10.5 Final Verification

A repair is not complete simply because a DTC has been cleared.

Final verification establishes that the original fault has been corrected and that the vehicle operates as intended.

### Professional post-repair procedure

* Confirm that the repair work is complete.

* Inspect all disturbed connectors, wiring and components.

* Confirm that the vehicle is correctly reassembled.

* Restore any required settings or service configurations.

* Perform the manufacturer's prescribed initialization or calibration, if required.

* Clear DTCs only when appropriate.

* Carry out the required functional test.

* Repeat the complete vehicle scan.

* Compare post-repair data with the original scan.

* Save the final diagnostic report.

### Before-and-after comparison

Simulated example

| Diagnostic item              | Before repair | After repair             |
| ---------------------------- | ------------- | ------------------------ |
| Cooling pump DTC             | Present       | Not present              |
| Pump command                 | 80%           | 80%                      |
| Pump feedback                | 0%            | 78%                      |
| Coolant temperature response | Abnormal      | Within OEM specification |
| System warning               | Active        | Not active               |

The figures are illustrative. Actual acceptable values depend on the vehicle and manufacturer.

Important: A DTC disappearing immediately after clearing is not sufficient verification. The relevant operating conditions and monitoring cycle must be completed as required by the OEM.

### Complete professional diagnostic workflow

### From customer complaint to verified repair

* Initial inspection

    Record symptoms, vehicle identity and safety condition.

* Complete vehicle scan

    Retrieve DTCs and identify communicating and unavailable ECUs.

* Fault analysis

    Examine DTC relationships, freeze-frame data and live data.

* Physical and electrical testing

    Verify suspected faults using suitable diagnostic instruments.

* Root-cause identification

    Establish the failed circuit, component or system condition.

* Repair

    Follow manufacturer procedures and safety requirements.

* Final verification

    Re-test, rescan and compare diagnostic evidence.

* Reporting

    Save the final report and document the repair outcome.

---

### Module 2 — OBD-II, CAN Bus & ECU Communication

### Lesson 2.1: Introduction to Automotive Communication Systems

In modern electric and hybrid vehicles, electronic control units must exchange information continuously to coordinate the powertrain, battery, braking, charging, thermal management and safety systems.

As a technician, you need to understand how these systems communicate because many vehicle faults are not caused by defective components, but by communication failures, incorrect data or network interruptions.

This lesson follows the four official sections in your handbook.

### 2.1.1 Purpose of Vehicle Networks

A vehicle network is an electronic communication system that allows different ECUs to exchange information.

Without vehicle networks, each ECU would require separate wiring connections to every other ECU with which it needed to communicate. This would create excessive wiring, weight, complexity and cost.

Vehicle networks provide a more efficient way to share information.

### Example: EV acceleration

When a driver presses the accelerator pedal, several systems must work together.

A simplified communication sequence:

* The accelerator pedal position sensor measures pedal movement.

* The relevant control system receives the accelerator position signal.

* The VCU calculates the requested driving torque.

* The VCU communicates the torque request to the motor controller.

* The motor controller controls inverter operation.

* The inverter supplies controlled three-phase electrical power to the traction motor.

* Other ECUs coordinate battery power limits, traction control and braking requirements.

The systems must exchange accurate information at the correct time.

### Main purposes of vehicle networks

| Purpose             | Explanation                                                 |
| ------------------- | ----------------------------------------------------------- |
| Data sharing        | Allows ECUs to exchange sensor and operating information    |
| System coordination | Coordinates different vehicle systems                       |
| Reduced wiring      | Reduces the need for individual point-to-point wiring       |
| Fault monitoring    | Allows systems to report communication and operating faults |
| Safety coordination | Supports coordinated responses to abnormal conditions       |
| Diagnostic access   | Allows diagnostic equipment to communicate with ECUs        |

Technician's point: A communication DTC does not automatically mean an ECU is defective. The problem may be in its power supply, ground, network wiring, connector or another communicating ECU.

### 2.1.2 Electronic Control Units (ECUs)

An Electronic Control Unit is an embedded electronic controller that monitors inputs, processes information and controls outputs.

An ECU normally contains:

* Microcontroller or processor.

* Memory.

* Power supply and voltage regulation.

* Input signal conditioning circuits.

* Output driver circuits.

* Communication transceivers.

* Software and calibration data.

### Basic ECU operating principle

INPUTS

Sensors, switches and messages from other ECUs

PROCESSING

Microcontroller executes software and control calculations

OUTPUTS

Actuators, control signals and messages to other ECUs

### Important EV and hybrid ECUs

| ECU                       | Main responsibility                              |
| ------------------------- | ------------------------------------------------ |
| VCU                       | Coordinates vehicle-level operation              |
| BMS                       | Monitors and manages the HV battery              |
| Inverter/Motor Controller | Controls electric motor operation                |
| OBC Controller            | Manages onboard AC charging functions            |
| DC-DC Controller          | Manages conversion from HV DC to low-voltage DC  |
| ABS/ESC ECU               | Controls braking and vehicle stability functions |
| BCM                       | Manages body electrical functions                |
| Thermal Management ECU    | Controls cooling and heating functions           |

The exact ECU names and functions vary by manufacturer.

### Example: Battery Management System

The BMS monitors parameters such as:

* Individual cell or cell-group voltages.

* Battery current.

* Battery temperatures.

* State of Charge (SoC).

* State of Health (SoH), where supported.

* Insulation monitoring information, depending on architecture.

It communicates relevant information to other controllers.

For example, if battery temperature or voltage conditions restrict available power, the BMS can communicate a power limitation to the VCU. The VCU can then coordinate the requested motor torque.

This is why communication between ECUs is essential to vehicle operation.

### 2.1.3 Distributed Control Architecture

Distributed control architecture means that vehicle control functions are shared among multiple ECUs instead of being handled by one central controller.

Each ECU has its own responsibilities, but it communicates with other controllers to coordinate vehicle operation.

### Example of a distributed EV architecture

A simplified representation:

Vehicle Control Unit (VCU)

Vehicle-level coordination

Communication network

BMS

Battery monitoring

Inverter ECU

Motor control

ABS/ESC

Braking and stability

OBC ECU

Charging control

Thermal Management ECU

Cooling and heating coordination

Simplified conceptual architecture. Actual network connections and control authority vary by vehicle.

### Advantages of distributed architecture

* Modularity: Each ECU performs specific functions.

* Scalability: Manufacturers can add or change vehicle functions.

* Local processing: Controllers can process their own sensor inputs and control outputs.

* Fault identification: Diagnostic systems can identify faults associated with individual controllers.

* System coordination: ECUs exchange information to coordinate complex functions.

### Diagnostic implications

A distributed architecture also introduces diagnostic challenges.

For example, if the VCU stops receiving valid information from the BMS, it may limit vehicle power or prevent the vehicle from entering READY mode.

Possible causes include:

* BMS power supply failure.

* Poor ECU ground.

* CAN wiring fault.

* Connector damage.

* Network termination problem.

* BMS internal failure.

* Incorrect or missing communication messages.

The correct diagnosis requires checking the entire communication path.

### 2.1.4 Communication Network Development

Automotive communication systems have developed as vehicle electronics have become more complex.

Earlier vehicles used relatively simple electrical connections. Modern vehicles use multiple communication protocols and network architectures.

### General development

| Network technology    | Main characteristics                                                   |
| --------------------- | ---------------------------------------------------------------------- |
| Point-to-point wiring | Direct electrical connection between devices                           |
| LIN                   | Low-cost, relatively low-speed communication for local components      |
| CAN                   | Robust serial communication widely used between automotive controllers |
| FlexRay               | Deterministic communication designed for time-critical applications    |
| Automotive Ethernet   | High-bandwidth communication for advanced vehicle systems              |

### LIN — Local Interconnect Network

LIN is commonly used for lower-cost local communication.

Examples include certain:

* Door modules.

* Seat control systems.

* Mirror adjustment systems.

* Climate-control actuators.

LIN is generally slower and simpler than CAN.

### CAN — Controller Area Network

CAN is a major automotive communication technology.

It allows multiple ECUs to communicate over a shared bus using message identifiers and arbitration.

It is widely used for powertrain, chassis and body-related communication.

We will study CAN in detail later in Module 2.

### FlexRay

FlexRay was developed for applications requiring predictable communication timing and high reliability.

It has been used in some advanced chassis and control applications.

### Automotive Ethernet

Automotive Ethernet provides higher data bandwidth for systems that transfer large quantities of information.

Examples include:

* Advanced driver assistance systems.

* Cameras and sensor systems.

* Infotainment.

* High-speed vehicle gateways.

* Modern zonal and central computing architectures.

Important: These technologies can coexist in one vehicle. A gateway may connect different network types and control the transfer of messages between them.

### Workshop diagnostic example: No communication with BMS

Simulated workshop case

Customer complaint: EV does not enter READY mode.

Scanner observation: VCU communicates, but BMS communication is unavailable.

Initial diagnostic reasoning:

* Confirm that the 12 V supply is stable.

* Check the BMS power supply and ground using the correct wiring diagram.

* Inspect BMS connectors and network wiring.

* Check communication signals using suitable diagnostic equipment.

* Confirm whether the BMS is powered and transmitting messages.

* Follow OEM diagnostic procedures before condemning the ECU.

Do not open or probe HV battery internals as part of this basic communication check. Follow OEM HV safety procedures and use appropriately rated equipment and authorized test points.

### Key technical terms

| Term             | Meaning                                                          |
| ---------------- | ---------------------------------------------------------------- |
| ECU              | Electronic Control Unit                                          |
| VCU              | Vehicle Control Unit                                             |
| BMS              | Battery Management System                                        |
| CAN              | Controller Area Network                                          |
| LIN              | Local Interconnect Network                                       |
| Gateway          | Controller that routes or manages communication between networks |
| Transceiver      | Electronic interface that sends and receives network signals     |
| Bus              | Shared communication pathway                                     |
| Network topology | Physical or logical arrangement of network devices               |

---

### Module 2 — OBD-II, CAN Bus & ECU Communication

### Lesson 2.2: OBD-II Architecture and Operation

OBD-II (On-Board Diagnostics II) is a standardized vehicle diagnostic system that allows external diagnostic equipment to retrieve emissions-related information, diagnostic trouble codes and operating data.

For an EV and hybrid technician, understanding OBD-II is essential because the diagnostic connector can provide access to vehicle information through standardized and manufacturer-specific communication systems.

Important distinction: OBD-II is not the same as the complete vehicle diagnostic system. A professional scanner may access many ECUs and functions that are outside standardized OBD-II requirements.

### 2.2.1 OBD-II Architecture

OBD-II architecture consists of several elements that work together to provide diagnostic access.

The main elements are:

* Vehicle sensors and monitored systems.

* Electronic Control Units (ECUs).

* Diagnostic software and communication interfaces.

* Diagnostic connector (DLC).

* External diagnostic scanner.

### Simplified architecture

Vehicle sensors and monitored systems

Temperature, pressure, voltage, speed and other signals

ECU

Monitors parameters and executes diagnostic logic

Vehicle communication network

CAN or another supported communication protocol

Diagnostic Link Connector (DLC)

Standardized diagnostic connection point

Diagnostic scanner

Requests and displays available diagnostic information

### How OBD-II works

Consider a monitored temperature sensor.

* The sensor provides an electrical signal to the ECU.

* The ECU converts the signal into a temperature value.

* The ECU compares the measured value with its programmed diagnostic criteria.

* If a monitored condition meets fault-detection criteria, the ECU may store a DTC.

* The scanner requests diagnostic information through the DLC.

* The ECU responds with supported information.

A fault code is therefore the result of the ECU's diagnostic logic. It does not necessarily identify the exact defective component.

### EV and hybrid application

OBD-II-related diagnostic access may provide information such as:

* Powertrain DTCs.

* Emissions-related monitor status.

* Supported live data.

* Freeze-frame data.

* Vehicle identification information.

Additional EV and hybrid information, such as individual battery cell voltages, inverter temperatures and manufacturer-specific power limits, may require enhanced OEM or multibrand diagnostic functions.

### 2.2.2 Diagnostic Connector Pins

The standard OBD-II connector is known as the 16-pin Diagnostic Link Connector (DLC).

The connector uses a standardized pin arrangement, although not every manufacturer uses every pin.

### Important DLC pin assignments

| Pin | Standardized function             |
| --- | --------------------------------- |
| 2   | SAE J1850 Bus +                   |
| 4   | Chassis ground                    |
| 5   | Signal ground                     |
| 6   | CAN High (ISO 15765-4)            |
| 7   | K-Line (ISO 9141-2 / ISO 14230-4) |
| 10  | SAE J1850 Bus −                   |
| 14  | CAN Low (ISO 15765-4)             |
| 15  | L-Line, where applicable          |
| 16  | Battery positive supply           |

Technician's note: Pins 6 and 14 are commonly used for high-speed CAN diagnostic communication. Pins 4 and 5 provide different ground references and should not be assumed interchangeable for every measurement.

### DLC electrical checks

Before connecting a scanner to a vehicle with suspected communication problems, inspect the connector and verify the relevant electrical conditions.

Pin 16 — Battery supply

A digital multimeter can be used to measure the supply voltage between pin 16 and an appropriate ground reference.

The measured voltage should be consistent with the vehicle's low-voltage electrical system and operating condition.

Pins 4 and 5 — Ground

Check the appropriate ground circuits using the manufacturer's procedures. A loaded voltage-drop test can reveal poor ground connections that a simple continuity check may miss.

Pins 6 and 14 — CAN

These are CAN differential communication lines on vehicles using the standardized CAN diagnostic connection.

Their electrical condition and signal behaviour will be covered in greater detail in Lessons 2.3 and 2.4.

Safety

Never apply battery voltage to communication pins. Do not use an insulation tester or high-voltage test equipment on DLC communication circuits.

### 2.2.3 Communication Protocols

A communication protocol defines how electronic devices exchange information.

It specifies matters such as:

* Electrical signalling.

* Message structure.

* Data transmission.

* Addressing.

* Error detection.

* Communication timing.

Several protocols have been used for OBD-II communication.

### Main OBD-II communication protocols

| Protocol      | Technical description                        |
| ------------- | -------------------------------------------- |
| SAE J1850 PWM | Pulse Width Modulation communication         |
| SAE J1850 VPW | Variable Pulse Width communication           |
| ISO 9141-2    | Serial diagnostic communication using K-Line |
| ISO 14230-4   | Keyword Protocol 2000 (KWP2000)              |
| ISO 15765-4   | Diagnostic communication over CAN            |

### CAN-based OBD-II communication

On a CAN-based vehicle, the scanner sends a diagnostic request through the DLC.

The request travels over the vehicle communication network to the relevant ECU or diagnostic gateway.

The ECU processes the request and returns a response.

For example, a scanner may request a supported engine or powertrain parameter using an OBD-II diagnostic service.

The ECU responds with data that the scanner decodes and displays.

### Why protocol identification matters

Suppose a scanner powers up when connected but cannot communicate with the vehicle.

Possible causes include:

* Incorrect vehicle selection.

* Unsupported communication protocol.

* Missing DLC power or ground.

* Damaged communication wiring.

* ECU power supply failure.

* Gateway access restrictions.

* Network faults.

A powered scanner does not prove that communication is working.

### 2.2.4 Diagnostic Service Modes

OBD-II diagnostic services are commonly called modes in traditional OBD-II terminology.

They define the type of diagnostic information being requested or the operation being performed.

The traditional OBD-II service modes include:

| Mode     | Function                                                       |
| -------- | -------------------------------------------------------------- |
| Mode $01 | Request current powertrain diagnostic data                     |
| Mode $02 | Request freeze-frame data                                      |
| Mode $03 | Request stored emission-related DTCs                           |
| Mode $04 | Clear/reset emission-related diagnostic information            |
| Mode $05 | Request oxygen sensor monitoring test results, where supported |
| Mode $06 | Request results of monitored on-board diagnostic tests         |
| Mode $07 | Request pending emission-related DTCs                          |
| Mode $08 | Request control of on-board systems, where supported           |
| Mode $09 | Request vehicle information                                    |
| Mode $0A | Request permanent emission-related DTCs                        |

### Mode $01 — Current diagnostic data

This mode retrieves supported current powertrain data.

Examples may include:

* Engine speed.

* Vehicle speed.

* Coolant temperature.

* Intake air temperature.

* Calculated load.

* Supported fuel-system information.

For a conventional hybrid, some engine-related parameters may be available. A battery-electric vehicle may support a different subset of standardized data.

### Mode $02 — Freeze-frame data

Freeze-frame data is a stored snapshot of operating conditions associated with a detected fault.

It may contain information such as:

* Vehicle speed.

* Engine speed, where applicable.

* Temperature.

* Calculated load.

* Other supported parameters.

This helps the technician understand the conditions under which the fault was detected.

### Mode $03 — Stored DTCs

Requests stored emission-related diagnostic trouble codes.

A scanner may display a code such as:

Illustrative example

### P0420

Catalyst System Efficiency Below Threshold (Bank 1)

This is an emissions-related example, not a general EV battery fault.

### Mode $04 — Clear/reset diagnostic information

This service requests clearing or resetting supported emission-related diagnostic information.

Clearing codes may also reset readiness-monitor information.

Professional rule: Save the original scan, freeze-frame data and relevant evidence before clearing codes.

### Mode $06 — On-board monitoring test results

This mode retrieves results from supported diagnostic monitoring tests.

It can be useful for investigating a monitored system that has not necessarily generated a confirmed DTC.

The scanner must correctly interpret the test identification, component identification and result values.

### Mode $07 — Pending DTCs

Requests pending emission-related fault codes.

These indicate detected fault conditions that have not necessarily met all criteria for confirmation.

### Mode $09 — Vehicle information

Can provide supported identification information, including:

* VIN.

* Calibration identification.

* Calibration verification information.

The exact available data depends on the vehicle.

### Mode $0A — Permanent DTCs

Requests permanent emission-related DTCs.

These codes are designed not to be removed simply by using a normal clear-code command or disconnecting the battery. Their removal generally depends on the vehicle successfully completing the required monitoring and confirming that the fault condition has been corrected.

Important: These standardized modes do not represent every function available through a professional scanner. Manufacturer-specific diagnostic services may provide access to much broader vehicle functions.

### 2.2.5 OBD-II Limitations

OBD-II is useful, but it does not provide complete diagnostic access to every vehicle system.

A technician must understand its limitations to avoid drawing incorrect conclusions.

### 1\. Limited ECU coverage

Standard OBD-II primarily focuses on emissions-related diagnostics.

A basic generic scanner may not access:

* Individual BMS cell data.

* Inverter internal temperatures.

* Battery contactor status.

* HV interlock status.

* Charging-system detailed parameters.

* Manufacturer-specific hybrid functions.

These often require enhanced diagnostic access.

### 2\. Limited manufacturer-specific information

Standardized DTC definitions and data do not cover all manufacturer-specific fault information.

An OEM diagnostic tool may provide:

* Detailed DTC descriptions.

* Additional fault subcodes.

* ECU-specific live data.

* Guided diagnostic procedures.

* Component tests.

* Software and configuration information.

### 3\. Limited active testing

A basic OBD-II reader normally focuses on retrieving standardized information.

It may not support bidirectional control of pumps, fans, relays, valves or other actuators.

### 4\. Limited programming access

Generic OBD-II access does not automatically provide the ability to:

* Flash ECU software.

* Perform ECU coding.

* Register replacement components.

* Carry out advanced calibrations.

* Execute security-authorized functions.

### 5\. Gateway and security restrictions

Some modern vehicles restrict access to diagnostic functions through secure gateways.

The technician may need manufacturer authorization or an approved diagnostic access method.

### Generic scanner versus professional diagnostic scanner

| Function                   | Basic generic scanner | Professional enhanced scanner                  |
| -------------------------- | --------------------- | ---------------------------------------------- |
| Standard OBD-II DTCs       | Usually               | Yes                                            |
| Standard live data         | Usually               | Yes                                            |
| Freeze-frame data          | Usually               | Yes                                            |
| Manufacturer-specific DTCs | Limited               | Often supported                                |
| BMS detailed data          | Usually limited       | Vehicle-dependent                              |
| Bidirectional tests        | Usually limited       | Vehicle-dependent                              |
| ECU coding                 | Usually unavailable   | Supported on selected vehicles                 |
| ECU programming            | Usually unavailable   | Requires compatible hardware and authorization |

### Practical workshop scenario

Simulated case

Vehicle: Battery-electric vehicle

Complaint: Dashboard displays a powertrain warning.

Scanner result: Generic OBD-II scanner communicates with the vehicle but reports no standardized emission-related DTCs.

Question: Does this prove the EV has no faults?

No.

The generic scanner may have accessed only the standardized diagnostic functions and may not have accessed the VCU, BMS, inverter or charging controller's enhanced diagnostic information.

### Correct diagnostic approach

* Confirm scanner compatibility.

* Perform a complete vehicle scan using a suitable enhanced diagnostic tool.

* Check ECU communication status.

* Retrieve manufacturer-specific DTCs.

* Review relevant freeze-frame and live data.

* Follow the applicable OEM diagnostic procedure.

The absence of a generic OBD-II fault code is not proof that the vehicle is fault-free.

### Key workshop reference

| Item     | What you should remember                 |
| -------- | ---------------------------------------- |
| DLC      | Standardized 16-pin diagnostic connector |
| Pin 16   | Low-voltage battery supply               |
| Pin 4    | Chassis ground                           |
| Pin 5    | Signal ground                            |
| Pin 6    | CAN High                                 |
| Pin 14   | CAN Low                                  |
| Mode $01 | Current diagnostic data                  |
| Mode $02 | Freeze-frame data                        |
| Mode $03 | Stored DTCs                              |
| Mode $04 | Clear/reset diagnostic information       |
| Mode $06 | On-board monitoring results              |
| Mode $07 | Pending DTCs                             |
| Mode $09 | Vehicle information                      |
| Mode $0A | Permanent DTCs                           |

---

### Module 2 — OBD-II, CAN Bus & ECU Communication

### Lesson 2.3: Controller Area Network (CAN Bus)

CAN stands for Controller Area Network. It is one of the most important communication technologies used in modern vehicles.

For an EV technician, understanding CAN is essential because the VCU, BMS, inverter, ABS, charging controller and other ECUs must exchange information reliably.

A CAN fault can cause multiple warning lights, communication DTCs, reduced power or even prevent a vehicle from entering READY mode.

This lesson covers the five official sections.

### 2.3.1 CAN Principles

CAN is a serial communication protocol originally developed for automotive applications. It allows multiple electronic control units to communicate over a shared network.

Instead of requiring a separate communication wire between every pair of ECUs, multiple controllers can connect to the same CAN bus.

### Basic CAN network architecture

A simplified network contains:

* CAN-H communication conductor.

* CAN-L communication conductor.

* Multiple ECU nodes.

* Termination resistors at the ends of the bus.

* CAN transceivers inside communicating ECUs.

Each ECU connects to the bus through a CAN transceiver.

The transceiver converts the controller's digital logic signals into electrical signals on the CAN network and converts received electrical signals back into digital information.

### How CAN communication works

Suppose the BMS needs to communicate a battery power limitation.

* The BMS measures battery operating conditions.

* Its controller calculates the permitted power limit.

* The BMS prepares a CAN message.

* The CAN transceiver transmits the message onto the network.

* Other ECUs receive the message.

* The VCU processes the information and adjusts the vehicle's operating strategy.

The message is available to network nodes, but each ECU processes only the messages relevant to its programmed functions.

### Important CAN characteristics

| Characteristic          | Explanation                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------ |
| Multi-master            | Multiple ECUs can initiate communication                                             |
| Message-based           | Information is transmitted in messages, not simply as a direct ECU-to-ECU connection |
| Broadcast               | Transmitted messages can be received by multiple network nodes                       |
| Arbitration             | Determines which message gains access when several ECUs transmit simultaneously      |
| Error detection         | CAN includes mechanisms for detecting transmission errors                            |
| Differential signalling | Uses the voltage difference between CAN-H and CAN-L                                  |

Important: CAN messages are generally identified by message identifiers, not by a simple destination address. The receiving ECUs decide which messages are relevant.

### 2.3.2 CAN High and CAN Low

A conventional high-speed CAN network uses two communication wires:

* CAN High (CAN-H).

* CAN Low (CAN-L).

These wires carry complementary electrical signals.

### Recessive state

In the recessive state, both lines are approximately at:

* CAN-H: 2.5 V.

* CAN-L: 2.5 V.

The voltage difference is approximately zero.

### Dominant state

In a typical high-speed CAN network, during the dominant state:

* CAN-H rises towards approximately 3.5 V.

* CAN-L falls towards approximately 1.5 V.

The differential voltage becomes approximately 2 V.

These are typical illustrative values for high-speed CAN, not universal specifications for every automotive network.

### Dominant versus recessive

| Condition | CAN-H | CAN-L | Differential voltage |
| --------- | ----- | ----- | -------------------- |
| Recessive | 2.5 V | 2.5 V | Approximately 0 V    |
| Dominant  | 3.5 V | 1.5 V | Approximately 2 V    |

The CAN bus uses the dominant state to represent a logical 0 and the recessive state to represent a logical 1.

### Why two wires?

The two-wire arrangement improves resistance to electrical interference.

External interference that affects both wires similarly can be rejected by the differential receiver, because it evaluates the voltage difference rather than relying only on either wire's voltage relative to ground.

This is particularly useful in vehicles containing:

* Electric traction motors.

* Inverters.

* DC-DC converters.

* High-current switching circuits.

* Battery charging equipment.

### 2.3.3 Differential Voltage Signalling

Differential signalling means that the receiver interprets the difference between two electrical signals.

The important measurement is:

`V_diff = V_CAN-H − V_CAN-L`

Where:

* `V_diff` = differential voltage.

* `V_CAN-H` = CAN High voltage.

* `V_CAN-L` = CAN Low voltage.

### Worked calculation 1 — Dominant state

Assume the oscilloscope or measurement equipment indicates:

`V_CAN-H = 3.5 V`

`V_CAN-L = 1.5 V`

Therefore:

`V_diff = 3.5 − 1.5 = 2.0 V`

This is a typical dominant-state differential voltage.

### Worked calculation 2 — Recessive state

Assume:

`V_CAN-H = 2.5 V`

`V_CAN-L = 2.5 V`

Therefore:

`V_diff = 2.5 − 2.5 = 0 V`

This is the typical recessive-state condition.

### Why differential signalling matters in EV diagnosis

Imagine an inverter generates electrical interference that affects both CAN conductors.

If the interference is approximately equal on both wires, the receiver can still distinguish the intended differential signal.

However, if one conductor becomes open-circuit, shorted or severely distorted, the differential signal may become unreliable.

Possible symptoms include:

* Lost communication DTCs.

* Intermittent ECU communication.

* Invalid or missing messages.

* Reduced power.

* Vehicle operating restrictions.

### Common-mode voltage

Another useful engineering concept is common-mode voltage.

`V_CM = (V_CAN-H + V_CAN-L) / 2`

Using the typical dominant-state values:

`V_CM = (3.5 + 1.5) / 2 = 2.5 V`

This is the average voltage of the two communication conductors relative to the measurement reference.

A receiver must tolerate an appropriate common-mode voltage range as defined by the transceiver specification.

### 2.3.4 CAN Message Structure

CAN does not transmit information as an unstructured collection of electrical pulses. It organizes information into frames.

A CAN frame contains defined fields that allow receiving controllers to identify, validate and process the transmitted information.

### Main fields of a classical CAN data frame

| Field         | Function                                                   |
| ------------- | ---------------------------------------------------------- |
| SOF           | Start of Frame; marks the beginning                        |
| Identifier    | Identifies the message and determines arbitration priority |
| Control field | Contains control information, including data length        |
| Data field    | Carries the actual information                             |
| CRC           | Cyclic Redundancy Check for error detection                |
| ACK           | Acknowledgment field                                       |
| EOF           | End of Frame                                               |

### 1\. Start of Frame (SOF)

The SOF indicates that a new CAN frame is beginning.

It uses a dominant bit.

### 2\. Identifier

The identifier provides message identification and establishes arbitration priority.

Classical CAN supports:

* 11-bit standard identifiers.

* 29-bit extended identifiers.

A lower numerical identifier has higher arbitration priority when competing identifiers are compared using the CAN arbitration process.

### 3\. Control field

The control field includes information such as the Data Length Code (DLC), which indicates the number of data bytes.

### 4\. Data field

In classical CAN, the data field can contain up to 8 bytes.

CAN FD (Flexible Data-Rate) supports larger payloads, up to 64 bytes.

### 5\. CRC field

CRC is used to detect certain transmission errors.

The receiving controller calculates and checks the frame's integrity.

### 6\. ACK field

The ACK field allows a receiving node that correctly receives the frame to acknowledge it.

The transmitting node checks whether the frame was acknowledged.

### 7\. End of Frame

The EOF field marks the end of the CAN frame.

### Example: CAN message carrying battery information

Illustrative simulated message

Example CAN data frame

| Parameter  | Example         |
| ---------- | --------------- |
| Identifier | 0x180           |
| Format     | Standard 11-bit |
| DLC        | 4 bytes         |
| Data       | 2A 01 64 00     |

This is an invented example to demonstrate frame structure. It is not a real vehicle message definition.

The meaning of the four data bytes cannot be determined from the frame alone.

You need the vehicle's CAN database or manufacturer documentation to establish:

* Which bits represent a parameter.

* Whether the data is signed or unsigned.

* Byte order.

* Scaling factor.

* Offset.

* Units.

* Valid range.

For example, a temperature signal might use a conversion formula:

`T = (Raw value × Scaling factor) + Offset`

Never assume the scaling or interpretation without the correct message definition.

### 2.3.5 Arbitration and Priority

CAN uses a process called non-destructive bitwise arbitration.

This allows multiple ECUs to begin transmitting simultaneously without corrupting the message from the highest-priority transmitter.

### Why arbitration is necessary

Imagine three ECUs want to transmit at the same time:

* BMS.

* VCU.

* ABS/ESC.

All three monitor the bus while transmitting.

If an ECU transmits a recessive bit but detects a dominant bit on the bus, it knows that another ECU is transmitting a higher-priority identifier.

The ECU that loses arbitration stops transmitting and waits for another opportunity.

The winning message continues without being corrupted.

### Example of arbitration

Simplified illustrative identifiers

Suppose three ECUs attempt to transmit these 11-bit identifiers:

| ECU   | Identifier | Priority |
| ----- | ---------- | -------- |
| ECU A | 0x080      | Highest  |
| ECU B | 0x180      | Second   |
| ECU C | 0x280      | Third    |

Arbitration result

ECU A — 0x080

Wins

Continues transmitting its complete message.

ECU B — 0x180

Waits

Stops transmitting when it detects that it has lost arbitration.

ECU C — 0x280

Waits

Also stops transmitting and retries later.

### Why does the lowest identifier win?

CAN uses dominant and recessive bit states:

* Dominant = logical 0.

* Recessive = logical 1.

During arbitration, dominant bits overwrite recessive bits on the bus.

A transmitter that sends a recessive bit but reads a dominant bit knows that another transmitter has higher priority.

For the three identifiers above:

```text
ECU A: 00000010000
ECU B: 00110000000
ECU C: 01010000000
```

The first differing bit determines which transmitter loses arbitration.

ECU A has the highest priority because its identifier has the lowest numerical value.

Important: Arbitration priority is determined by the identifier, not by which ECU is physically closest to the bus or which ECU starts first.

### Diagnostic significance

If high-priority messages occupy too much network capacity, lower-priority messages may experience delays.

This can become important when diagnosing:

* Network overload.

* Excessive message traffic.

* Incorrect ECU configuration.

* Faulty communication behaviour.

* Timing-related communication problems.

### Workshop application: Diagnosing a CAN communication fault

Simulated case

Vehicle complaint: EV displays a powertrain warning and enters reduced-power mode.

Scanner results:

| ECU      | Communication status |
| -------- | -------------------- |
| VCU      | Communicating        |
| BMS      | Communicating        |
| Inverter | Intermittent         |
| ABS/ESC  | Communicating        |
| OBC      | Communicating        |

### Initial technical interpretation

The intermittent communication with the inverter may indicate a problem affecting its network connection, power supply or internal communication interface.

It does not prove that the inverter itself is defective.

### Diagnostic direction

* Save the complete vehicle scan.

* Identify which network carries inverter communication.

* Check the inverter's low-voltage power supply and ground.

* Inspect its network connector and wiring.

* Examine CAN-H and CAN-L using an appropriate oscilloscope.

* Compare the waveform with the manufacturer's specifications.

* Check for network errors and communication interruptions.

* Follow the OEM diagnostic procedure before deciding on a repair.

The detailed electrical tests for termination resistance, voltage measurements, open circuits, shorts and waveform analysis are covered in Module 2.4.

### Key workshop reference

| Concept               | Essential point                                |
| --------------------- | ---------------------------------------------- |
| CAN                   | Multi-node automotive communication protocol   |
| CAN-H                 | High-side communication conductor              |
| CAN-L                 | Low-side communication conductor               |
| Recessive             | Typical CAN-H and CAN-L both near 2.5 V        |
| Dominant              | Typical CAN-H near 3.5 V and CAN-L near 1.5 V  |
| Differential voltage  | CAN-H minus CAN-L                              |
| Standard identifier   | 11 bits                                        |
| Extended identifier   | 29 bits                                        |
| Classical CAN payload | Up to 8 bytes                                  |
| CAN FD payload        | Up to 64 bytes                                 |
| Arbitration           | Lower numerical identifier has higher priority |
| CRC                   | Detects transmission errors                    |

---

<!-- NEXT: Module 2 — Lesson 2.4 CAN Bus Electrical Diagnosis (append below) -->
