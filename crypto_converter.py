import argparse


def main():
    """
    Main function
    Returns:

    """
    args = parse_arguments()
    try:
        result = convert(args.amount, args.from_unit.upper(), args.to_unit.upper())
        print(f"{args.amount} {args.from_unit.upper()} = {result:.6f} {args.to_unit.upper()}")
    except ValueError as e:
        print(e)


def parse_arguments():
    """
    Parse the command line arguments.
    Returns: The parsed arguments.

    """
    parser = argparse.ArgumentParser(
        description='Convert an amount between various cryptocurrencies and CHF.')
    parser.add_argument('amount', type=float, nargs='?', help='The amount to be converted.')
    parser.add_argument('from_unit', nargs='?', help='The unit of the input amount.')
    parser.add_argument('to_unit', nargs='?', help='The unit of the desired output.')
    parser.add_argument('-a', '--amount', type=float, required=False,
                        help='The amount to be converted.')
    parser.add_argument('-f', '--from', dest='from_unit', default='CHF',
                        help='The unit of the input amount. Default is "CHF".')
    parser.add_argument('-t', '--to', dest='to_unit', default='CHF',
                        help='The unit of the desired output. Default is "CHF".')

    args = parser.parse_args()
    return args


def convert(amount, from_unit, to_unit):
    """
    Convert an amount between various cryptocurrencies and CHF.
    Args:
        amount:
        from_unit:
        to_unit:

    Returns: The converted amount.

    """
    # Exchange rates relative to CHF
    exchange_rates = {
        'CHF': 1.00,
        'BTC': 97560.753,
        'ETH': 3078.24,
        # Add more cryptocurrencies and their rates to CHF as needed
    }
    # Check if the units are in the exchange rates dictionary
    if from_unit not in exchange_rates:
        raise ValueError(f'Unknown currency: {from_unit}')
    if to_unit not in exchange_rates:
        raise ValueError(f'Unknown currency: {to_unit}')

    # Convert amount to CHF
    amount_in_chf = amount * exchange_rates[from_unit]
    # Convert CHF to target currency
    converted_amount = amount_in_chf / exchange_rates[to_unit]
    return converted_amount


if __name__ == "__main__":
    main()
