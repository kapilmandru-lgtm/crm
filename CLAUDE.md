# CRM Project Documentation

## Overview
Mandrudi CRM - S4Us Logistics & Vitsco Integration Project

## Current Focus
S4Us Logistics - Outbound Delivery & Picking Slip Requirement

### Topic Summary
- **Project:** S4Us Logistics OB VT Prioritize & Identify Deliveries in Shipping
- **Goal:** Implement a new picking slip solution for warehouse delivery management
- **Problem:** Warehouse operators need to identify which HUs (Handling Units) belong to the same delivery during staging
- **Solution Approach:** Physical picking slip document with barcode (Recommended)

### Key Solution Alternatives
1. ✅ **Print physical document** (Recommended by BU) - Similar to picking slip with delivery barcode
2. Digital system with delivery-specific handling
3. Digital picking list triggered when HU is scanned
4. Larger screen for tablet/desktop picking list

## Important Meeting
📅 **Date:** Thursday (Do.), 16:30 (4:30 PM)
- **Topic:** S4Us Logistics | Vitsco Integration | Outbound | Working Session
- **Duration:** ~1 hour (3:30 PM - 4:30 PM based on calendar)
- **Attendees:** Felix, Torsten, Walter
- **Key Discussion Points:**
  - Which of the four solution alternatives should be pursued
  - Do we need aggregated picking slip functionality?
  - Constraints (tablet availability, RF scanner limitations)
  - Alignment with Vitsco Inbound, SALES delivery monitoring, CDTRs
- **Owner:** FISCHER, TORSTEN

## Requirements Details

### Picking Slip - Header Level Information
- TO number (also as barcode)
- Outbound delivery number (also as barcode)
- Plant
- Warehouse number
- Movement type (S4Us: Warehouse process type)
- Number of TO items

### Picking Slip - Item Level Information
- Item number
- Material and description
- LPK if the material has an LPK and the flag "Print" is set
- Picking storage location
- Storage unit type (SUT)
- Stock category
- Special stock number
- Package ID or Storage Unit (also as barcode)
- Quantity
- GR date
- Source and destination storage bin

## Next Steps
- [ ] Prepare for Thursday 16:30 meeting
- [ ] Review the 4 solution alternatives
- [ ] Gather input from team on preferred approach
- [ ] Define requirements for SolMan entry
