```mermaid
%%{init: {'theme': 'forest'} }%%
classDiagram
      OutputWriter --o WalletMainService
      WalletMainService --o WalletMainController
      WalletAPIService --o WalletMainService
      TxGetter --o WalletMainService
      TxGetter <|-- TxGetterScan
      ToAnalyse -- WalletMainController
      ChainData -- WalletMainController
      class ToAnalyse {
        <<Config>>
      }
      class ChainData {
        <<Config>>
      }
```
