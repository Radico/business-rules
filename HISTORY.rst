History
-------

1.6.2
+++++
released 2020-09-28

- Renamed project to business-rules-simon to fix naming conflicts

1.6.1
+++++
released 2020-09-14

- Removed check for method type when validating parameters

1.6.0
+++++
released 2020-09-03

- Added a disable_checks flag to disable the rules engine from doing extra input validation
- Made all numeric comparisons use `float` not `Decimal` for speed
- Defaulted to NOT assert_type_for_arguments as that can slow down processing
- Standardized rule params to use `field_type` and `default_value` for their parameters
- Allowed the `default_value` for a parameter to be optional

1.0.1
+++++
released 2016-3-16

- Fixes a packaging bug preventing 1.0.0 from being installed on some platforms.

1.0.0
+++++
released 2016-3-16

- Removes caching layer on rule decorator
