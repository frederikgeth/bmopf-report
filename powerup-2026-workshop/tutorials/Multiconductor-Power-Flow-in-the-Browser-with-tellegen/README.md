# Multiconductor AC power flow in the browser with tellegen

Solve the IEEE 13 node test feeder, three-phase and unbalanced, with nothing installed.
You need a current browser and the two files in this folder. Checked live on tellegen.dev
on September 11, 2026: converged in 14 iterations, about 0.3 s.

## Files

- `ieee13.bmopf.json`: IEEE 13 in draft BMOPF 0.2 JSON, converted from the OpenDSS
  distribution's `IEEE13Nodeckt.dss` with PowerIO 0.11.1
  (`powerio convert IEEE13Nodeckt.dss --to bmopf-json -o ieee13.bmopf.json`), then edited in
  two places so tellegen's power flow accepts it: the closed switch between buses 671 and 692
  is written as a 0.3048 m line of linecode `mtx601`, because the fixed-point snapshot has no
  switch model, and every bus carries per-terminal `v_min` and `v_max` at 0.9 and 1.1 of
  nominal phase-to-ground voltage, which gives the regulator windings their voltage base. The
  file validates against the draft 0.2.0 schema.
- `ieee13.geo.json`: the published bus layout from `IEEE13Node_BusXY.csv` as a GeoJSON
  `FeatureCollection`: one `Point` per bus (`properties.bus`), one `LineString` per line
  (`properties.bus_from`, `bus_to`), and `"powerio_geo": {"space": "diagram"}` because these
  are drawing coordinates, not longitude and latitude. tellegen reports 16 buses and 12
  routes matched.
- `NOTICE-OPENDSS-BSD-3-CLAUSE`: license of the source feeder data.

## Steps

1. Open <https://tellegen.dev>.
2. Use **drop a case file** in the header and select both files at once, or drag them onto
   the page. PowerIO, compiled to WebAssembly, classifies the JSON by content and opens the
   multiconductor viewer with the feeder drawn in its published layout. The files stay on
   your device; nothing is uploaded.
3. The Network panel shows `IEEE13Nodeckt`, 16 buses, 19 branches, and **Solve AC power
   flow**. Choose it, or open **Studies** and choose **Run power flow**; both run the same
   calculation.
4. Read the summary: status Converged, 14 iterations, voltage band Valid, load voltage range
   0.897 to 1.005 pu, source P and Q about 3521 kW and 1808 kvar, passive loss about 124 kW.
5. Pick a bus under **Bus result** for each terminal's voltage to ground and to neutral in
   volts and degrees, and its net current in amperes. Pick a branch under **Branch result**
   for conductor currents and terminal powers.
6. **Save result** keeps the study in this browser; **Export** downloads a snapshot.

## What the solver does and does not do

The solver is a fixed-point iteration around one sparse complex LU factorization. It updates
compensated load currents until both voltage changes and KCL residuals meet tolerance, and
reports convergence and voltage validity separately.

Supported: constant power, constant current, constant impedance, ZIP, and exponential loads;
two-winding transformers; fixed-tap single-phase autotransformer regulators.

Not supported today: switches (write them as short lines), multiconductor AC OPF, regulator
and inverter controls, generator or inverter injections, finite source impedance, transformers
with more than two windings. Raw OpenDSS `.dss` files open view-only; convert them to BMOPF.

## Bring your own feeder

```
cargo install powerio-cli
powerio convert my_feeder.dss --to bmopf-json -o my_feeder.bmopf.json
```

The writer reports every field the BMOPF schema cannot hold. Give each bus `v_min` and
`v_max`, and replace closed switches with short lines, as above. To place a feeder on the
map instead of a diagram, write `"powerio_geo": {"space": "geographic"}` and give
coordinates as `[longitude, latitude]`.

## Provenance

The IEEE 13 node test feeder ships with the OpenDSS distribution (EPRI, BSD 3-Clause; see the
notice file). Draft BMOPF 0.2 remains subject to Task Force review.
