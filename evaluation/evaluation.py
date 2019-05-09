class Evaluation:
    weights = {
        "have_ip": 10,
        "netloc_too_long": 5,
        "have_unusual": 10,
        "in_phish_tank": 80,
        "have_redirect": 15,
        "low_pr": 5,
        "create_less_3_month": 15,
        "have_script": 5,
        "abnormal_time": 10,
        "inducible_title": 30,
        "inducible_content": 20,
        "unusual_size": 10,
        "trick_type": 30
    }

    limit = 20

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
