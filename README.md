# Ethereum ETL

###  ETL

1. 自定义csv格式  将ethereum-etl工具导出的blocks.csv和transactions.csv合并

   blocks.csv

   | Column            | Type       |
   | ----------------- | ---------- |
   | number            | bigint     |
   | hash              | hex_string |
   | parent_hash       | hex_string |
   | nonce             | hex_string |
   | sha3_uncles       | hex_string |
   | logs_bloom        | hex_string |
   | transactions_root | hex_string |
   | state_root        | hex_string |
   | receipts_root     | hex_string |
   | miner             | address    |
   | difficulty        | numeric    |
   | total_difficulty  | numeric    |
   | size              | bigint     |
   | extra_data        | hex_string |
   | gas_limit         | bigint     |
   | gas_used          | bigint     |
   | timestamp         | bigint     |
   | transaction_count | bigint     |
   | base_fee_per_gas  | bigint     |

   transactions.csv

   | Column                   | Type       |
   | ------------------------ | ---------- |
   | hash                     | hex_string |
   | nonce                    | bigint     |
   | block_hash               | hex_string |
   | block_number             | bigint     |
   | transaction_index        | bigint     |
   | from_address             | address    |
   | to_address               | address    |
   | value                    | numeric    |
   | gas                      | bigint     |
   | gas_price                | bigint     |
   | input                    | hex_string |
   | block_timestamp          | bigint     |
   | max_fee_per_gas          | bigint     |
   | max_priority_fee_per_gas | bigint     |
   | transaction_type         | bigint     |

   合并后的block.csv 本质是将transactions.csv文件中的每一个transaction作为其所在block中的一个字段放入blocks.csv中

   | Column            | Type       |
   | ----------------- | ---------- |
   | number            | bigint     |
   | hash              | hex_string |
   | parent_hash       | hex_string |
   | nonce             | hex_string |
   | sha3_uncles       | hex_string |
   | logs_bloom        | hex_string |
   | transactions_root | hex_string |
   | state_root        | hex_string |
   | receipts_root     | hex_string |
   | miner             | address    |
   | difficulty        | numeric    |
   | total_difficulty  | numeric    |
   | size              | bigint     |
   | extra_data        | hex_string |
   | gas_limit         | bigint     |
   | gas_used          | bigint     |
   | timestamp         | bigint     |
   | transaction_count | bigint     |
   | base_fee_per_gas  | bigint     |
   | transaction1      |            |
   | transaction2      |            |
   | ...               |            |

2. 实时更新

   1. 监控 区块的生成 ethereum-etl的stream操作
   2. 导出 将新生成的区块 在原始工具的基础上 做1中的合并操作 追加到合并后的blocks.csv文件中

## demo

查询实例 各两个 参考诏贤师兄项目的例子和算法

1. 静态
2. 动态

## dataset（备选）

1. mock服务
2. 原始数据导出（时间 网络传输）

