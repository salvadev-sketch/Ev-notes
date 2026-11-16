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

<!-- NEXT: Lesson 1.6 — Freeze-Frame and Live Data Analysis (append below) -->
