import re


class AmharicNormalizer:
    def __init__(self):
        self.replacements = {
            "ሀ": "ሃ", "ሐ": "ሃ", "ሓ": "ሃ", "ኅ": "ሃ", "ኻ": "ሃ", "ኃ": "ሃ",
            "ዅ": "ሁ", "ሗ": "ኋ", "ኁ": "ሁ", "ኂ": "ሂ", "ኄ": "ሄ", "ዄ": "ሄ", "ኅ": "ህ",
            "ኆ": "ሆ", "ሑ": "ሁ", "ሒ": "ሂ", "ሔ": "ሄ", "ሕ": "ህ", "ሖ": "ሆ", "ኾ": "ሆ",
            "ሠ": "ሰ", "ሡ": "ሱ", "ሢ": "ሲ", "ሣ": "ሳ", "ሤ": "ሴ", "ሥ": "ስ", "ሦ": "ሶ",
            "ዐ": "አ", "ዑ": "ኡ", "ዒ": "ኢ", "ዓ": "አ", "ኣ": "አ", "ዔ": "ኤ", "ዕ": "እ",
            "ዖ": "ኦ", "ፀ": "ጸ", "ፁ": "ጹ", "ጺ": "ፂ", "ጻ": "ፃ", "ጼ": "ፄ", "ፅ": "ጽ",
            "ፆ": "ጾ", "ሼ": "ሸ", "ሺ": "ሽ", "ዲ": "ድ", "ጄ": "ጀ", "ጂ": "ጅ", "ዉ": "ው",
            "ዎ": "ወ", "ቼ": "ቸ", "ቺ": "ች", "ዬ": "የ", "ዪ": "ይ", "ጬ": "ጨ",
            "ጪ": "ጭ", "ኜ": "ኘ", "ኚ": "ኝ", "ዤ": "ዠ", "ዢ": "ዥ",
            "ሉ[ዋአ]": "ሏ", "ሙ[ዋአ]": "ሟ", "ቱ[ዋአ]": "ቷ", "ሩ[ዋአ]": "ሯ",
            "ሱ[ዋአ]": "ሷ", "ሹ[ዋአ]": "ሿ", "ቁ[ዋአ]": "ቋ", "ቡ[ዋአ]": "ቧ",
            "ቹ[ዋአ]": "ቿ", "ሁ[ዋአ]": "ኋ", "ኑ[ዋአ]": "ኗ", "ኙ[ዋአ]": "ኟ",
            "ኩ[ዋአ]": "ኳ", "ዙ[ዋአ]": "ዟ", "ጉ[ዋአ]": "ጓ", "ደ[ዋአ]": "ዷ",
            "ጡ[ዋአ]": "ጧ", "ጩ[ዋአ]": "ጯ", "ጹ[ዋአ]": "ጿ", "ፉ[ዋአ]": "ፏ",
            "[ቊ]": "ቁ", "[ኵ]": "ኩ", r"\s+": " ",
        }

    def normalize(self, text: str) -> str:
        """
        Normalization for Amharic text.
        Add any specific normalization rules or transformations here.
        """
        for pattern, replacement in self.replacements.items():
            text = re.sub(pattern, replacement, text)

        return text