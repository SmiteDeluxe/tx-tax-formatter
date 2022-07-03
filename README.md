```mermaid
classDiagram
      WalletMainService <|-- WalletMainController
      WalletAPIService <|-- WalletMainService
      TxProcessor <|-- WalletMainService
      OutputWriter <|-- WalletMainService
      Chains_and_Wallets_to_test <|-- WalletMainController
      ChainsInfo <|-- WalletMainController
      class Chains_and_Wallets_to_test {
        <<Config>>
      }
      class ChainsInfo {
        <<Config>>
      }
```
