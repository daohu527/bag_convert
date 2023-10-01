# bag_convert
Ros bag to Apollo record or reverse conversion

# Install
You can install `bag_convert` with the following command
```
pip3 install bag_convert
```

# Quick start
```
-m bag conversion mode(b2r, r2b)
-b bag_file 
-r record_file
```
## Ros bag to Cyber record
```shell
bag_convert -m=b2r -b=data/input.bag -r=data/output.record
```

## Cyber record to Ros bag
```shell
bag_convert -m=r2b -r=data/input.record -b=data/output.bag
```
