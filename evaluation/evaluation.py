class Evaluation:
    weights = {
        "have_ip": 15,
        "netloc_too_long": 7.5,
        "have_unusual": 10,
        "in_phish_tank": 80,
        "have_redirect": 12.5,
        "low_pr": 5,
        "create_less_3_month": 17.5,
        "have_script": 5,
        "abnormal_time": 12.5,
        "inducible_title": 17.5,
        "inducible_content": 25,
        "unusual_size": 12.5,
        "trick_type": 30
    }

    limit = 15

    @classmethod
    def evaluate(cls, report):
        score = 0.0

        for chunk in report:
            count = report[chunk]["count"]
            if count > 0:
                for item in report[chunk]:
                    if item != "count" and report[chunk][item]["count"] > 0:
                        score += cls.weights[item] * report[chunk][item]["count"] / count

        if score > 100:
            score = 100
        return score
