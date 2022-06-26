# xml-traansformations-python
Study example for working with xml in spark

## Pre-requisites

We use [`batect`](https://batect.dev/) to dockerise the tasks in this exercise. 
`batect` is a lightweight wrapper around Docker that helps to ensure tasks run consistently (across linux, mac windows).
With `batect`, the only dependencies that need to be installed:
* Docker
* Java >= (1.8)

## Run tests

### Run tests
```bash
./batect test
```

## Run style checks
```bash
./batect lint
```

## Job

For each id in the dataset, parse xml document by following paths.
- /SINGLE_FORMAT/INQUIRIES/INQUIRY/INQ_PERIOD
- /SINGLE_FORMAT/INQUIRIES/INQUIRY/INQ_PURPOSE
- /SINGLE_FORMAT/INQUIRIES/INQUIRY/INQ_AMT
- /SINGLE_FORMAT/INQUIRIES/INQUIRY/INQ_CURRENCY
- /SINGLE_FORMAT/INQUIRIES/INQUIRY/INQ_QTY
- /SINGLE_FORMAT/INQUIRIES/INQUIRY/INQ_OWN


#### Input
Directory with `*.parquet` files with following schema:
```
id: long
response_xml: string
```

#### Output
A single `*.parquet` file with following schema:
```
INQ_PERIOD: array<int>
INQ_PURPOSE: array<int>
INQ_AMT: array<int>
INQ_CURRENCY: array<int>
INQ_QTY: array<int>
INQ_OWN: array<int>
```

#### Run the job

```bash
./batect run 
```
