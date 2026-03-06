use std::{error::Error, fs, path::{Path, PathBuf}};
use polars::prelude::*;

fn main() {
    let path=fs::canonicalize("../../../../datasets").expect("path does not exist");
    // let data=LazyFrame::scan_parquet_files(input_files.into(), 
    //     Default::default()).unwrap().collect()?;
    // println!("{:?}", input_path.exists());
}

